
from .models import Tournament, TournamentPlayer, Player, Match
from django.http import JsonResponse
from core.decorators import token_required
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
import math
import json


def isWhole(x):
    if(x % 1 == 0):
        return True
    else:
        return False


def reset_db(request):
    MODELS = [Tournament, Player, TournamentPlayer, Match]
    for Model in MODELS:
        Model.objects.all().delete()
    return JsonResponse({"ok": "ok"})


@token_required
def home_view(request):
    tour_choice = ['tania', 'Not started', 'Started', 'Completed']
    if request.method == 'GET':
        tour = Tournament.objects.filter(creator=request.swiss_user)
        tour_l = []
        for item in tour.all():
            tour_d = [str(item.id), item.name, tour_choice[item.status]]
            tour_l.append(tour_d)
        return JsonResponse({'data': tour_l})
    elif request.method == 'POST':
        req_body = json.loads(request.body.decode('utf-8'))
        tournament_name = req_body['name']
        try:
            tournament = Tournament.objects.get(name=tournament_name,
                                                creator=request.swiss_user)
            return JsonResponse({'error': 'tournament is already present'}, status=400)
        except ObjectDoesNotExist:
            tournament = Tournament.objects.create(name=tournament_name,
                                                   creator=request.swiss_user)
            return JsonResponse({'id': tournament.id , 'name': tournament.name, 'status': tour_choice[tournament.status]})
    else:
        pass


@token_required
def player_view(request, tour_id):
    if request.method == 'GET':
        player = Player.objects.filter(creator=request.swiss_user)
        player_l = []
        for item in player.all():
            player_d = item.name
            player_l.append(player_d)
        return JsonResponse({'data': player_l})
    elif request.method == 'POST':
        req_body = json.loads(request.body.decode('utf-8'))
        tour = Tournament.objects.get(id=tour_id)
        tournament_name = tour.name
        status = tour.status
        if status == 1:
            try:
                name = req_body['playername']
                if name == "":
                    return JsonResponse({'error': 'please provide a name for a player'},status=400)
                try:
                    player = Player.objects.get(name=name,
                                                creator=request.swiss_user)
                    return JsonResponse({'error' :'player is already present'},status=400)
                except ObjectDoesNotExist:
                    player = Player.objects.create(name=name,
                                                   creator=request.swiss_user
                                                  )
                    tournament_obj = Tournament.objects.get(name=tournament_name,
                                                            creator=request.swiss_user)
                    TournamentPlayer.objects.create(tournament=tournament_obj,
                                                    player=player)
                    return JsonResponse({'name': player.name})
            except Exception:
                player_id = req_body['player_id']
                try:
                    player = Player.objects.get(id=player_id)
                    return JsonResponse({'error' :'player is already present'},status=400)
                except Exception:
                    return JsonResponse({'error': 'no entry in database, please provide name to create'},status=400)
        else:
            return JsonResponse({'error':'cannot add player now'},status=400)


@token_required
def tour_status(request, tour_id):
    tournament = Tournament.objects.get(id=tour_id, creator=request.swiss_user)
    status = tournament.status
    if int(status) == 1:
        player_number = TournamentPlayer.objects.filter(tournament=tournament).count()
        n = math.log(player_number, 2)
        if player_number == 1:
            return JsonResponse({'status': status, 'error': 'add player for starting a match'},status=400)
        elif isWhole(n):
            return JsonResponse({'status': 'ready for starting the match' ,'tournament': tour_id, 'player_number': player_number})
        else:
            return JsonResponse({'status': status, 'error': 'add player for starting a match'},status=400)
    elif int(status) == 2:
        return JsonResponse({'status': 'In Progress'})
    elif int(status) == 3:
        return JsonResponse({'status': 'completed'})



@token_required
def standing_view(request, tour_id):
    tournament = Tournament.objects.get(id=tour_id, creator=request.swiss_user)
    round_id = tournament.current_round
    player_standing = tournament.player_standing(round_id)
    playerstand = []
    for key,value in player_standing[0].items():
        playerstand.append(value)
    return JsonResponse({'data': playerstand})


@token_required
def swiss_pairing(request, tour_id):
    tournament = Tournament.objects.get(id=tour_id, creator=request.swiss_user)
    round_id=tournament.current_round
    player_no = TournamentPlayer.objects.filter(tournament=tournament).count()
    n = math.log(player_no, 2)
    if isWhole(n):
        player_match = tournament.swiss_pairing(round_id)
        player = []
        winner = []
        for key, value in player_match.items():
            player_list = []
            player1 = Player.objects.get(id=int(key))
            player_list.append(player1.name)
            winner.append(player1.name)
            player2 = Player.objects.get(id=int(value))
            player_list.append(player2.name)
            player.append(player_list)
        return JsonResponse({'swiss_pairing': player, 'winner': winner})
    else:
        return JsonResponse({'error': "you don't have player no power of 2"})



@token_required
def report_match(request, tour_id, round_id):
    tournament = Tournament.objects.get(id=tour_id)
    games = tournament.report_match(round_id)
    final_list=[]
    for item in games:
        name_list=[]
        for i in item:
            player = Player.objects.get(id=i)
            name_list.append(player.name)
        final_list.append(name_list)
    return JsonResponse({'matchdetails': final_list})



@token_required
def player_details(request, tour_id):
    tournament = Tournament.objects.get(id=tour_id, creator=request.swiss_user)
    player = TournamentPlayer.objects.filter(tournament=tournament)
    player_l = []
    for item in player.all():
        player_d = item.player.name
        player_l.append(player_d)
    return JsonResponse({'data': player_l})




@token_required
def status_match(request, tour_id):
    tournament = Tournament.objects.get(id=tour_id, creator=request.swiss_user)
    list = ['notplayed','play','view']
    if request.method == 'GET':
        details = []
        round_id=tournament.current_round
        status = 2
        # match=Match.objects.filter(round=round_id)
        # if match:
        #     status = list[1]
        # else:
        #     status = list[2]
        details.append(round_id-1)
        details.append(list[status])

    return JsonResponse({'status':details})



@token_required
def round_view(request, tour_id):
    tournament = Tournament.objects.get(id=tour_id, creator=request.swiss_user)
    round_id = tournament.current_round
    player_no = TournamentPlayer.objects.filter(tournament=tournament).count()
    max_round = int(math.log(player_no, 2))
    roundlist = []
    if round_id <= max_round:
        for x in range(1, round_id+1):
            if x == round_id:
                b_list = []
                b_list.append(x)
                b_list.append('Play')
            else:
                b_list = []
                b_list.append(x)
                b_list.append('View')
            roundlist.append(b_list)
        for i in range(1, max_round+1):
            if i > round_id:
                roundlist.append(i)
    else:
        for i in range(1,round_id):
            b_list = []
            b_list.append(i)
            b_list.append('View')
            roundlist.append(b_list)
    return JsonResponse({'data': roundlist})


@token_required
def match_data(request, tour_id):
    req_body = json.loads(request.body.decode('utf-8'))
    player1_name = req_body['player1']
    playerone = Player.objects.get(name=player1_name, creator=request.swiss_user)
    player1 = playerone.id
    player2_name = req_body['player2']
    playertwo = Player.objects.get(name=player2_name, creator=request.swiss_user)
    player2 = playertwo.id
    winner_name = req_body['winner']
    winner = Player.objects.get(name=winner_name, creator=request.swiss_user)
    winner_id = winner.id
    tournament = Tournament.objects.get(id=tour_id, creator=request.swiss_user)
    round_id = tournament.current_round
    check = tournament.has_played_before(player1,player2)
    if check:
        tournament.conduct_match(round_id, player1, player2, winner_id)
    Tournament.objects.filter(id=tour_id).update(status=2)
    no_of_player = TournamentPlayer.objects.filter(tournament=tournament).count()
    n = int(no_of_player / 2)
    max_round = int(math.log(no_of_player, 2))
    totalmatch = max_round*n
    no_of_match= Match.objects.filter(tournament=tournament, round=round_id).count()
    if no_of_match == n:
        if round_id <= max_round:
            Tournament.objects.filter(id=tour_id).update(current_round=round_id+1)
    no_of_totalmatch = Match.objects.filter(tournament=tournament).count()
    if no_of_totalmatch == totalmatch:
        Tournament.objects.filter(id=tour_id).update(status=3)
    return JsonResponse({'data':'Match Played'})



@token_required
def current_round(request, tour_id):
    tournament = Tournament.objects.get(id=tour_id, creator=request.swiss_user)
    round_id = tournament.current_round
    return JsonResponse({'round_id':round_id })
