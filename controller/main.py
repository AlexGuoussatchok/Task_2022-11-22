from model.player import FootballPlayer
from model.manager import Manager


def main():
    leo = FootballPlayer("Leo", "Messi", 910, 450)
    cristiano = FootballPlayer("Cristiano", "Ronaldo", 840, 300)
    alex = FootballPlayer("Alessandro", "Del Pierro", 750, 800)
    ivan = FootballPlayer("Ivan", "Ivanov")

    players = (leo, cristiano, alex, ivan)

    player = Manager.give_golden_boll(players)

    print(player)


if __name__ == "__main__":
    main()
