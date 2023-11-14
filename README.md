# Automated Planning Course Assignment

## Description

This example is taken from the Assignment for the course "Automated Planning: Theory and Practice". Its original aim was to model planning problems in PDDL and show how can be integrated within the PlanSys2 library. We will use the PlanSys2 Terminal to insert commands. Actions simulate their execution.

## How to run

In terminal 1:

```
ros2 launch assignment assignment_launch.py
```

In terminal 2:

```
ros2 run plansys2_terminal plansys2_terminal        # enters in PlanSys2 Terminal

set instance robot1 robot

set instance p1 person
set instance p2 person
set instance p3 person
set instance p4 person
set instance p5 person
set instance p6 person

set instance c1 crate
set instance c2 crate
set instance c3 crate
set instance c4 crate
set instance c5 crate
set instance c6 crate

set instance depot location
set instance l1 location
set instance l2 location
set instance l3 location

set instance medicine content
set instance food content
set instance beverage content

set instance carrier1 carrier

set predicate (robot_at robot1 depot)
set predicate (free robot1)
        
set predicate (carrier_at carrier1 depot)
        
set predicate (person_at p1 l1) 
set predicate (person_at p2 l1)
set predicate (person_at p3 l1) 
set predicate (person_at p4 l2)
set predicate (person_at p5 l2) 
set predicate (person_at p6 l3)

set predicate (crate_at c1 depot) 
set predicate (crate_at c2 depot) 
set predicate (crate_at c3 depot) 
set predicate (crate_at c4 depot) 
set predicate (crate_at c5 depot) 
set predicate (crate_at c6 depot) 
        
set predicate (contain c1 medicine) 
set predicate (contain c2 food) 
set predicate (contain c3 beverage) 
set predicate (contain c4 medicine) 
set predicate (contain c5 food) 
set predicate (contain c6 beverage)

set predicate (available c1) 
set predicate (available c2)
set predicate (available c3) 
set predicate (available c4)
set predicate (available c5) 
set predicate (available c6)

set predicate (need p1 food)
set predicate (need p1 beverage)
set predicate (need p3 medicine)
set predicate (need p4 food)
set predicate (need p5 medicine)
set predicate (need p6 beverage)

set predicate (have p1 medicine) 
set predicate (have p2 food) 
set predicate (have p3 beverage)

set function (= (capacity carrier1) 4)

set goal (and (have p1 food) (have p1 beverage) (have p3 medicine) (have p4 food) (have p5 medicine) (have p6 beverage))

get plan                                              # Creates plan and shows it
run                                                   # Creates plan and runs it
```
