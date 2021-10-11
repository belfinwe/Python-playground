from dataclasses import dataclass

@dataclass
class PlayingCard:
    """
    The meaning of the syntax is similar to the function
    decorators. In the example above, you could have
    done the decoration by writing
    PlayingCard = dataclass(PlayingCard).
    """
    rank: str
    suit: str


if __name__ == "__main__":
    a = PlayingCard(rank="two", suit="heart")

    print(a)
    print(type(a))
    print(a.rank)
    print(a.suit)

