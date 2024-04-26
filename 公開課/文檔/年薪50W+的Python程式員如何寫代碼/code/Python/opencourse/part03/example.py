"""
撲克
"""
import enum
import random


@enum.unique
class Suite(enum.Enum):
    """花色(枚舉)"""
    SPADE, HEART, CLUB, DIAMOND = range(4)


class Card:
    """牌"""

    def __init__(self, suite, face):
        self.suite = suite
        self.face = face

    def __repr__(self):
        suites = '♠♥♣♦'
        faces = ['', 'A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
        return f'{suites[self.suite.value]}{faces[self.face]}'


class Poker:
    """撲克"""

    def __init__(self):
        self.cards = [Card(suite, face) for suite in Suite
                      for face in range(1, 14)]
        self.current = 0

    def shuffle(self):
        """洗牌"""
        self.current = 0
        random.shuffle(self.cards)

    def deal(self):
        """發牌"""
        card = self.cards[self.current]
        self.current += 1
        return card

    @property
    def has_next(self):
        """還有沒有牌可以發"""
        return self.current < len(self.cards)


def main():
    """主函數（程序入口）"""
    poker = Poker()
    poker.shuffle()
    print(poker.cards)


if __name__ == '__main__':
    main()
