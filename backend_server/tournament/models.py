from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from itertools import tee


def grouped(list1):
    return zip(list1[0::2], list1[1::2])


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


TOURNAMENT_STATUS_CHOICES = (
    (1, 'NOT STARTED'),
    (2, 'STARTED'),
    (3, 'COMPLETED')
)


class Tournament(models.Model):
    name = models.CharField(max_length=100)
    creator = models.ForeignKey(User)
    status = models.IntegerField(choices=TOURNAMENT_STATUS_CHOICES, default=1)
    current_round = models.IntegerField(default=1)

    def __str__(self):
        return '{} - {} - Status: {}'.format(
            self.name,
            self.creator,
            self.status
        )

    def player_standing(self, round_id):
        self.p_list = []
        self.player_standing = {}
        self.swiss_paring_dict = {}
        for item in self.players.all():
            self.player_name = item.player.name
            self.player_id = item.player.id
            if round_id == 0:
                self.match_no = 0
                self.win_no = 0
            else:
                self.match_no = self.games.filter((Q(player_one=self.player_id) | Q(player_two=self.player_id)) & Q(round__lt=round_id)).count()
                self.win_no = self.games.filter(Q(winner=self.player_id) & Q(round__lt=round_id)).count()
            self.lose_no = self.match_no - self.win_no
            self.player_list = []
            self.player_list.append(self.player_name)
            self.player_list.append(self.match_no)
            self.player_list.append(self.win_no)
            self.player_list.append(self.lose_no)
            self.player_standing[self.player_id] = self.player_list
            self.swiss_paring_dict[self.player_id] = self.win_no
        self.p_list.append(self.player_standing)
        self.p_list.append(self.swiss_paring_dict)
        return self.p_list

    def swiss_pairing(self, round_id):
        self.player_match = {}
        self.player_list = self.player_standing(round_id)
        self.player_dict = self.player_list[1]
        if round_id == 1:
            self.id_list = list(sorted(self.player_dict))
            for var1, var2 in grouped(self.id_list):
                self.player_match[var1] = var2

        else:
            self.order_list = sorted(self.player_dict.items(),
                                     key=lambda kv: kv[1], reverse=True)
            self.id_list = []
            for item in self.order_list:
                self.id_list.append(item[0])

            already_paired = []
            print(self.id_list)
            for i in self.id_list:
                index_value = self.id_list.index(i)
                if i not in already_paired:
                    for j in self.id_list[index_value + 1:]:
                        if j not in already_paired:
                            self.value = self.has_played_before(i, j)
                            if self.value:
                                self.player_match[i] = j
                                already_paired.append(i)
                                already_paired.append(j)
                                break
        #     print(self.player_match)

        # else:
        #     self.order_list = sorted(self.player_dict.items(),
        #                              key=lambda kv: kv[1], reverse=True)
        #     self.id_list = []
        #     for item in self.order_list:
        #         self.id_list.append(item[0])
        #     for var1, var2 in grouped(self.id_list):
        #         a = self.id_list.index(var1)
        #         self.value = self.has_played_before(var1, var2)
        #         if self.value:
        #             self.player_match[var1] = var2
        #         else:
        #             self.n = self.id_list.index(var2)
        #             for item2 in self.id_list[self.n + 1:]:
        #                 var2 = item2
        #                 b = self.id_list.index(var2)
        #                 self.value = self.has_played_before(var1, var2)
        #                 if self.value:
        #                     self.player_match[var1] = var2
        #                     break
        return self.player_match

    def has_played_before(self, player1, player2):
        self.match_no = self.games.filter(Q(Q(player_one= player1) & Q(player_two= player2)) | Q(Q(player_one=player2) & Q(player_two=player1))).count()
        if self.match_no:
            return False
        else:
            return True

    def conduct_match(self, round_id, player1, player2, winner):
        self.games.create(status=2, round=round_id,
                          player_one_id=player1, player_two_id=player2,
                          tournament_id=self.id, winner_id=winner
                          )
        return self.games

    def report_match(self, round_id):
        self.matches = self.games.filter(round=round_id)
        report = []
        status = []
        for item in self.matches.all():
            match_details = []
            match_details.append(item.player_one_id)
            match_details.append(item.player_two_id)
            match_details.append(item.winner_id)
            report.append(match_details)
        return report

    def has_played(self,player,round_id):
        self.match_no = self.games.filter(Q(Q(player_one=player) | Q(player_two=player)) & Q(round=round_id)).count()
        if self.match_no:
            return False
        else:
            return True


    class Meta:
        unique_together = ('creator', 'name')


class Player(models.Model):
    name = models.CharField(max_length=50)
    creator = models.ForeignKey(User)

    class Meta:
        unique_together = ('name', 'creator')

    def __str__(self):
        return '{} - {}'.format(self.name, self.creator)


class TournamentPlayer(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='players')
    player = models.ForeignKey(Player)

    class Meta:
        unique_together = ('tournament', 'player')


MATCH_STATUS_CHOICES = (
    (1, 'UPCOMING'),
    (2, 'CONDUCTED')
)


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, related_name='games')
    status = models.IntegerField(choices=MATCH_STATUS_CHOICES, default=1)
    round = models.IntegerField()
    player_one = models.ForeignKey(Player, related_name='player_one')
    player_two = models.ForeignKey(Player, related_name='player_two')
    winner = models.ForeignKey(Player, related_name='winner')

    def __str__(self):
        return '{} {}'.format(
            self.tournament,
            self.round
        )
