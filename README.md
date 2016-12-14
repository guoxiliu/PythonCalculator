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

| Keyword       | Usage                 |
|---------------|-----------------------|
| **out**       | output result         |
| **define**    | declare a variable    |
| **function**  | to declare a function |
| **return**    | return to caller      |
| **if**        | implement branch      |
| **else**      | implement branch      |
| **true**      | boolean value         |
| **false**     | boolean value         |

#### Identifier 
##### Built-in identifier 

| Name  | Value         |
|-------|---------------|
| **pi**| 3.14159265359 |
| **e** | 2.71828182846 |

##### Usage 
- All identifier begins with letters (A-Z or a-z) 
- There can be letters or underscore after the first character
- Identifier is case-sensitive 
- Identifier can not be reserved keyword 
- It is okay to change the value of built-in indentifier
- Valid identifier: age, length_of_table 
- Invalid indentifier: _age, lengt1_of_table 

#### Operators 
##### Arithmetic operators 

| Operators | Name      | Example       | Precedence |
|-----------|:----------|:--------------|:----------:|
| \*        | time      | 3 \* 5 = 15   | 1          |
| /         | divide    | 20 / 10 = 2   | 1          |
| %         | mod       | 40 % 3 = 1    | 1          |
| ^         | power     | 9 ^ 2 = 81    | 1          |
| \+        | plus      | 1 + 1 = 2     | 2          |
| \-        | minus     | 13 - 6 = 7    | 2          |

##### Relational operators 

| Operators | Name                      | Example       | Precedence |
|-----------|:--------------------------|:--------------|:----------:|
| \>=       | greater than or equal to  | 5 >= 3        | 1          |
| <=        | less than or equal to     | 2 <= 4        | 1          |
| ==        | equal to                  | 2 == 2        | 1          |
| !=        | not equal to              | 1 != 0        | 1          |
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
sample code: 

```
define a = 10.5; 
define b = 4; 
out(a + b); 
out(a - b); 
out(a * b); 
out(a / b); 
```
sample output: 

```
14.5 
6.5 
42.0 
2.625 
```

##### Logical laws 
sample code: 

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
sample output: 

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
sample code: 

```
define x = 1; 
define y = 2; 
if (x < y) { 
	out(x); 
} 
```
sample output: 

```
1.0 
```

##### IF-ELSE 
sample code: 

```
define x = 1; 
define y = 2; 
if (x == y) { 
	out(x);	
} else { 
	out(y); 
} 
```
sample output: 

```
2.0 
```

#### Loop 
sample code: 

```
define a = 2; 
while (a < 5) { 
    a = a + 1; 
    out(a); 
} 
```
sample output: 

```
3.0 
4.0 
5.0 
```

### Function 
#### Define a function 
sample code: 

```
function abs(num) { 
    if (num < 0) { 
        return (0 - num); 
    } else { 
        return num; 
    } 
} 
 
function factorial(number) { 
    if (number == 1) { 
        return 1; 
    } else { 
        return number * test(number - 1); 
    } 
} 
```

#### Call a function 
##### Built-in functions 
sample code: 

```
out(sin(pi/6)); 
out(cos(pi/3)); 
out(tan(pi/4)); 
out(sinh(0.5)); 
out(cosh(0.5)); 
out(tanh(1)); 
out(ln(e^3)); 
out(lg(1000)); 
out(sqrt(169)); 
```
sample output: 

```
0.5 
0.5 
1.0 
0.521095305494 
1.12762596521 
0.761594155956 
3.04858735157 
13.0 
```

##### Self-defined functions 
sample code: 

```
out(abs(-5)); 
out(abs(-6.78)); 
out(factorial(5)); 
out(factorial(3)); 
```
sample output: 

```
5.0 
6.78 
120.0 
6.0 
```

## **Error Handling**
### Lexical analyzer