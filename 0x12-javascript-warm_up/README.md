![JavaScript Logo](https://live.staticflickr.com/3701/19224697601_6b600f21eb.jpg)

# 0x12. Javascript - Warm up

**Version 1.0.0**

Code and document samples for the 0x12-javascript-warm_up repository. 

## How To Use

#### Installation

Install Node 10
```
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

#### Clone Git Repository

Clone `holbertonschool-higher_level_programming`
```
$ git clone https://github.com/kellyhodis/holbertonschool-higher_level_programming.git
```

#### Navigate to Directory

```
$ cd holbertonschool-higher_level_programming/0x12-javascript-warm_up
```

#### Running The Files

##### Run `0-javascript_is_amazing.js`:

Print text to the screen.

`./0-javascript_is_amazing.js`

##### Run `1-multi_languages.js`:

Print three lines of text to the screen.

`./1-multi_languages.js`

##### Run `2-arguments.js`:

Print a message depending on number of arguments passed.

`./2-arguments.js`

`./2-arguments.js One`

`./2-arguments.js One Two`

##### Run `3-value_argument.js`:

Print the first argument passed to script.

`./3-value_argument.js`

`./3-value_argument.js Word`

##### Run `4-concat.js`:

Print two arguments connected with "is".

`./4-concat.js this this`

`./4-concat.js this`

`./4-concat.js`

##### Run `5-to_integer.js`:

Print "My Number: `<first argument>`" if the first argument passed to the script can be converted to an integer.

`./5-to_integer.js`

`./5-to_integer.js 1`

`./5-to_integer.js Not`

##### Run `6-multi_languages_loop.js`:

Print three lines of text to the screen using an array and a loop.

`./6-multi_languages_loop.js`

##### Run `7-multi_c.js`:

Print "C is fun" times an integer provided to the script.

`./7-multi_c.js 4`

##### Run `8-square.js`:

Print a square of width and length size of an integer provided to the script.

`./8-square.js 3`

##### Run `9-add.js`:

Print the addition of two integers provided to the script.

`./9-add.js 2 4`

##### Run `10-factorial.js`:

Print the factorial of an integer provided to the script.

`./10-factorial.js 7`

##### Run `11-second_biggest.js`:

Print the second biggest integer in a list of integers provided to the script.

`./11-second_biggest.js 1 2 3 4`

##### Run `12-object.js`:

Update a value inside a `const` object.

`./12-object.js`

##### Run `13-add.js`:

Return the addition of two integers using import.

```
node
> const add = require('./13-add').add;
> console.log(add(1, 2));
```

##### Run `100-let_me_const.js`:

Modify the value of an object inside another file.

```
node
> myVar = 89;
> require('./100-let_me_const');
> console.log(myVar);
```

##### Run `101-call_me_moby.js`:

Execute a function times an integer provided to the script.

```
node
> const callMeMoby = require(./101-call_me_moby').callMeMoby;
> callMeMoby(7, function () {
    console.log(' 0 ');
  });
```

##### Run `102-add_me_maybe.js`:

Increments and calls a function.

```
node
> const addMeMaybe = require(./102-add_me_maybe').addMeMaybe;
> addMeMaybe(3, function(nb) {
    console.log('New: ' + nb);
  });
```

##### Run `103-object_fct.js`:

Add an object method to increment the integer value property of myObject.

`./103-object_fct.js`

## Contributors

- Kelly Hodis <668@holbertonschool.com>

## Holberton School
<a href="url" alt="Holberton logo"><img src="https://lh4.googleusercontent.com/yUzaviDgzDIq4-ZHp9k0YU5fsz0nOdekNRt1qHgp7Qdlw5BNfe6bETEf5ZWd-Vkn_m57BPx7HcDrwFK41ptLnQLTNipWmTAtiQwZL_8s97Nkzn94xP7XVKb3RnV0fx8QEZoxlkVd" width="350"></a>
