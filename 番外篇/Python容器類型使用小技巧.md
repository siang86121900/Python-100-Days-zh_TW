## Python容器類型使用小技巧

Python中提供了非常豐富的容器型數據類型，大家最為熟悉的有`list`、`tuple`、`set`、`dict`等。下麵為大家分享一些使用這些類型的小技巧，希望幫助大家寫出更加Pythonic的代碼。

### 從字典中取最大

假設字典對象對應的變數名為`my_dict`。

- 取出最大值

    ```Python
    max(my_dict.values())
    ```

- 取值最大值的鍵

    ```Python
    max(my_dict, key=my_dict.get)
    ```

- 取出最大值的鍵和值

    ```python
     max(my_dict.items(), key=lambda x: x[1])
    ```

    或

    ```Python
    import operator
    
    max(my_dict.items(), key=operator.itemgetter(1))
    ```
    
    > **說明**：上麵用到了`operator`模塊的`itemgetter`函數，這個函數的的作用如下所示。在上麵的代碼中，`itemgetter`幫我們獲取到了二元組中的第2個元素。
    >
    > ```Python
    > def itemgetter(*items):
    >     if len(items) == 1:
    >         item = items[0]
    >         def g(obj):
    >             return obj[item]
    >     else:
    >         def g(obj):
    >             return tuple(obj[item] for item in items)
    >     return g
    > ```

### 統計列錶元素出現次數

假設列錶對象對應的變數名為`my_list`。

```Python
{x: my_list.count(x) for x in set(my_list)}
```

或

```Python
from itertools import groupby

{key: len(list(group)) for key, group in groupby(sorted(my_list))}
```

> **說明**：`groupby`函數會將相鄰相同元素分到一個組中，所以先用`sorted`函數排序就是為了將相同的元素放到一起。

或

```Python
from collections import Counter

dict(Counter(my_list))
```

### 截斷列錶元素

假設列錶對象對應的變數名為`my_list`，通常大家會想到用下麵的方式來截斷列錶。
```Python
my_list = my_list[:i]
my_list = my_list[j:]
```

然而，更好的方式使用下麵的操作，大家可以認真想想為什麼。

```Python
del my_list[i:]
del my_list[:j]
```

### 按最長列錶實現zip操作

Python的內置函數`zip`可以産生一個生成器對象，該生成器對象將兩個或多個可叠代對象的元素組裝到一起，如下所示。

```Python
list(zip('abc', [1, 2, 3, 4]))
```

執行上麵的代碼會得到一個如下所示的列錶，相信大家也註意到了，列錶中元素的個數是由`zip`函數中長度最小的可叠代對象決定的，所以下麵的列錶中隻有3個元素。

```Python
[('a', 1), ('b', 2), ('c', 3)]
```

如果希望由`zip`函數中長度最大的可叠代對象來決定最終叠代出的元素個數，可以試一試`itertools`模塊的`zip_longest`函數，其用法如下所示。

```Python
from itertools import zip_longest

list(zip_longest('abc', [1, 2, 3, 4]))
```

上麵的代碼創建出的列錶對象如下所示。

```Python
[('a', 1), ('b', 2), ('c', 3), (None, 4)]
```

### 快速拷貝一個列錶

如果希望快速拷貝一個列錶對象，可以通過切片操作來實現，但是切片操作僅實現了淺拷貝，簡單的說就是切片創建了新的列錶對象，但是新列錶中的元素是和之前的列錶共享的。如果希望實現深拷貝，可以使用`copy`模塊的`deepcopy`函數。

- 淺拷貝

    ```Python
    thy_list = my_list[:]
    ```

    或

    ```Python
    import copy
    
    thy_list = copy.copy(my_list)
    ```

- 深拷貝

    ```Python
    import copy
    
    thy_list = copy.deepcopy(my_list)
    ```

### 對兩個或多個列錶對應元素進行操作

Python內置函數中的`map`函數可以對一個可叠代對象中的元素進行“映射”操作，這個函數在批量處理數據時非常有用。但是很多人都不知道，這個函數還可以作用於多個可叠代對象，通過傳入的函數對多個可叠代對象中的對應元素進行處理，如下所示。

```Python
my_list = [11, 13, 15, 17]
thy_list = [2, 4, 6, 8, 10]
list(map(lambda x, y: x + y, my_list, thy_list))
```

上麵的操作會得到如下所示的列錶。

```Python
[13, 17, 21, 25]
```

當然，同樣的操作也可以用`zip`函數配合列錶生成式來完成。

```Python
my_list = [11, 13, 15, 17]
thy_list = [2, 4, 6, 8, 10]
[x + y for x, y in zip(my_list, thy_list)]
```

### 處理列錶中的空值和零值

假設列錶對象對應的變數名為`my_list`，如果列錶中有空值（`None`）和零值，我們可以用下麵的方式去掉空值和零值。

```Python
list(filter(bool, my_list))
```

對應的列錶生成式文法如下所示。

```Python
[x for x in my_list if x]
```

### 從嵌套列錶中抽取指定列

假設`my_list`是一個如下所示的嵌套列錶，該嵌套列錶可以用來錶示數學上的矩陣，如果要取出矩陣第一列的元素構成一個列錶，我們可以這樣寫。

```Python
my_list = [
    [1, 1, 2, 2],
    [5, 6, 7, 8],
    [3, 3, 4, 4],
]
col1, *_ = zip(*my_list)
list(col1)
```

這裏我們會得到一個如下所示的列錶，剛好是矩陣的第一列。

```Python
[1, 5, 3]
```

以此類推，如果想取出矩陣第二列的元素構成一個列錶，可以用如下所示的方法。

```Python
_, col2, *_ = zip(*my_list)
list(col2)
```

至此，如果要實現矩陣的轉置操作，我們也可以按照上麵的思路寫出下麵的代碼。

```Python
[list(x) for x in zip(*my_list)]
```

經過上麵的操作，我們會得到如下所示的列錶。

```Python
[[1, 5, 3], 
 [1, 6, 3], 
 [2, 7, 4], 
 [2, 8, 4]]
```

### 小結

不知道上麵的內容有冇有觸及到大家的知識盲區，如果有的話歡迎在評論區留言討論。

  