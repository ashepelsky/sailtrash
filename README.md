# sailtrash

## Player Ship "Board" i.e. Ship interface

The ship has next properties:

1. Sail Level Indicator
2. Turn Indicator
3. Crew Points Hub
4. Hull integrity Bar
5. Speed Bar
6. Inertia Bar

### Sail Level Indicator
  Posibble values - `[0:4]`
  
### Turn Indicator
  Possible values - `[0:4]`

  There are left and right indicators as a separated entities.

### Crew Points Hub
  Possible values - `[0:15]`

### Hull integrity bar
  Possbile values - `[0:15]`
  
### Speed Bar
  Possbile values - `[0:12]`
  The values from Speed bar called `Moves`
  
### Inertia Bar
  Possbile values - `[0:12]`


## Player Actions

The table of possbile actions, their effects and price:

Ship Actions: 

1. Rise\Lower Sail | allows interaction with `Sail Level Indicator` | Price 2 `CP`
2. Turn | allows interaction with `Turn Indicator` | Base price 2 `CP`. Next action price = Base price + Previous invocation count

Game Interaction:

1. Move - use `Move` point from `Speed Bar` to `Move` the ship for 1 tile. Reduces value of the Speed Bar by 1.
2. End Turn - Finishes current turn


## Action points (Crew Points)

The Crew Points (CP) are used to pay a cost for executing a Ship Action.
Action is an interaction between a player and a ship. The player can not move ship directly, it is done only via invoking actions like `Rise\Lower Sail` or `Turn`.


## Movement

### Speed and Inertia

Note: Speed is an indication of how many `Moves` player has and how much is left. After a move `Speed` is reducing by 1.

Inertia Level = `I`
Moves (Speed) =` M`
Sails Level = `S`
Wind Multiplicator = `W`

At the start of the game:

`I = 0`

**At the start of a round:**

`I = S * W + I`
AND
`M = I`

**At the end of Round:**

`I = I / 2` (round to the smaller number)


## Turn order

At the start of the game player has:

`CP = 10`
`Sail = 0`
`Turn Left = 0`
`Turn Right = 0`

**Order:**
 1. Resolve `Speed and Inertia` start of the round.
 2. `Move` OR spend `CP`
 3. Chech if `Speed` = 0
 4. If no, back to step 2
 5. If yes, end the round.
 6. Resolve `Speed and Inertia` end of the round.

**Explanation:**

At the beggining of the round calculatuons from `Speed and Inertia` occure. Because of the `Sail = 0` starting value Ship will gain no Speed.
Next, player chooses how to spent a CP. Player may decide to `Rise Sails`. This will allow to gain `Moves`.

If the `Speed` is equal to 0, round may be finished. All speed **MUST** be resolved.

Lets say that the player decided to set a `Sail` to **3**.
Wind in this example will be **1**.

Then on next round we have next Speed and Inertia:

``` 
I = 3 * 1 + 0
I=3
M=I
M=3
```

As a result, player gained **3** move points which must be spent this turn. Inertia will remain the same until the end of the round. At the end the value will be **1**. See `Speed and Inertia` section.

Lets calculate the speed and inertia for round 3. Assume that player did not change a `Sail`

``` 
I = 3 * 1 + 1
I=4
M=I
M=4
```


