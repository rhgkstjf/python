# 1.1 특별메소드

### 특별메소드는 `__init__` 과같은 앞뒤에 이중 언더바를 가지는 메소드    
### Ex) obj[key] 형태의 구문은 __getitem__() 메소드가 지원한다.    
#### 특별 메소드는 우리가 구현한 기본적인 언어 구조체를 구현하고 지원하며 함께 사용할 수 있게 도와준다.    
1. 반복
2. 컬렉션
3. 속성 접근
4. 연산자 오버로딩
5. 함수 및 메서드 호출
6. 객체 생성 및 제거
7. 문자열 표현 및 포맷
8. 블록 등 콘텍스트 관리



```python
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]
        
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position):
        return self._cards[position]


```


```python
beer_card = Card('7', 'diamonds')
```


```python
beer_card
```




    Card(rank='7', suit='diamonds')



#### 요부분에서 특별메소드가 무엇인지 바로 깨달을 수 있었다.    
기본적으로 사용자 정의 클래스의 메소드를 호출 할 땐 obj.methodName() 요런 형식이다.    
그런데, 해당 구문을보면 len() 이것은 파이썬 내장 함수인데, deck이라는 오브젝트를 파라미터로 넘겻을 때 작동한다.       
어떻게.? `__init__` 과같이 특별 메소드이기 때문이다.    
<a> https://docs.python.org/ko/3/library/functions.html#len 파이선 내장 함수 __len()__ 정보</a>   


```python
deck = FrenchDeck()
len(deck)
```




    52




```python
deck[0]
deck[-1]
```




    Card(rank='A', suit='hearts')



파이썬은 시퀸스에서 항목을 무작위로 뽑는 `random.choice()` 메소드를 제공한다.    
deck 객체에 적용하면 choice 메소드가 적용된다.


```python
from random import choice
choice(deck)
```




    Card(rank='8', suit='spades')




```python
choice(deck)
```




    Card(rank='8', suit='diamonds')




```python
choice(deck)
```




    Card(rank='4', suit='clubs')



#### 이로써 특별 메소드의 장점을 알게되었다.
* 사용자가 표준 연산을 수행하기 위해 클래스 자체에서 구현한 임의 메서드명을 외울 필요가없다.    
* 파이썬 표준 라이브러리에서 제공하는 풍부한 기능을 별도로 구현할 필요 없이 바로 사용가능하다.


```python
deck[:3]
deck[12::13]
```




    [Card(rank='A', suit='spades'),
     Card(rank='A', suit='diamonds'),
     Card(rank='A', suit='clubs'),
     Card(rank='A', suit='hearts')]




```python
for card in deck: # break , 모두 출력하면 쓸데없이 길어진다.
    print(card)
    break
```

    Card(rank='2', suit='spades')
    


```python
for card in reversed(deck):
    print(card)
    break
```

    Card(rank='A', suit='hearts')
    


```python
Card('Q', 'hearts') in deck
```




    True




```python
Card('7', 'beasts') in deck
```




    False




```python
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]
```


```python
for card in sorted(deck, key=spades_high):
    print(card)
    break
```

    Card(rank='2', suit='clubs')
    

특별 메소드는 파이썬 인터프리터가 호출하기 위한 것이라는 점을 알고있어야한다.    
위의 코드에서 my_object.__len__()으로 직접 호출하지 않고, len(my_object) 형태로 호출된다.    
만일 my_object가 사용자 정의 클래스 객체면 파이썬은 우리가 구현한 __len__()객체 메서드를 호출한다.    
