# **Calculator**
***
## **Introduction**
This project is to build a simple programmable calculator, 
which has its own programming language, and is very easy to learn.
## **Prerequisite**
- Build language: Python 2.7
- Package: ply

## **Language**
### Basic grammar
#### Reserved keyword

| Keyword   | Usage                 |
|---------  |-----------------------|
| out       | output result         |
| define    | declare a variable    |
| function  | to declare a function |
| return    | return to caller      |
| if        | implement branch      |
| else      | implement branch      |
| true      | boolean value         |
| false     | boolean value         |

#### Identifier
- All identifier begins with letters (A-Z or a-z)
- There can be letters or underscore after the first 
- Identifier is case-sensitive
- Identifier can not be reserved keyword
- Valid identifier: age, length_of_table
- Invalid indentifier: _age, lengt1_of_table

#### Operators
##### Arithmetic operators

| Operators | Name      | Example       | Precedence |
|-----------|:----------|:--------------|:----------:|
| \*        | time      | 3 \* 5 = 15   | 1          |
| /         | divide    | 20 / 10 = 2   | 1          |
| %         | mod       | 40 % 3 = 1    | 1          |
| \+        | plus      | 1 + 1 = 2     | 2          |
| \-        | minus     | 13 - 6 = 7    | 2          |

##### Relational operators

| Operators | Name                      | Example       | Precedence |
|-----------|:--------------------------|:--------------|:----------:|
| \>=       | greater than or equal to  | 5 >= 3        | 1          |
| <=        | less than or equal to     | 2 <= 4        | 1          |
| ==        | equal to                  | 2 == 2        | 2          |
| \>        | greater than              | 9 > 8         | 2          |
| <         | less than                 | 6 < 7         | 2          |

##### Logical operators

| Operators | Name | Example                | Precedence |
|-----------|------|------------------------|:----------:|
| !         | not  | !(true) = false        | 1          |
| &&        | and  | true && false =  false | 2          |
| &#124;&#124;| or   | true &#124;&#124; false = true | 2|

### Structures
#### Sequential 
##### Arithmetic laws

- sample code: 

``` 
define a = 10.5; 
define b = 4; 
out(a + b); 
out(a - b); 
out(a * b); 
out(a / b); 
```

- sample output: 

```
14.5 
6.5 
42.0 
2.625 
```

##### Logical laws

- sample code: 

```
define x = true; 
define y = false; 
out(x && x); 
out(y && y); 
out(x && y); 
out(x || x); 
out(y || y); 
out(x || y); 
```

- sample output: 

```
True 
False 
False 
True 
False 
True 
```

#### Branch
##### IF 


## Error Handling
### Lexical analyzer
