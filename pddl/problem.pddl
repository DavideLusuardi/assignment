(define (problem assignment)
  (:domain assignment)
  (:objects
    robot1 - robot
    p1 - person
    p2 - person
    p3 - person
    p4 - person
    p5 - person
    p6 - person
    c1 - crate
    c2 - crate
    c3 - crate
    c4 - crate
    c5 - crate
    c6 - crate
    depot - location
    l1 - location
    l2 - location
    l3 - location
    medicine - content
    food - content
    beverage - content
    carrier1 - carrier
  )
  (:init
    (robot_at robot1 depot)
    (free robot1)
    (carrier_at carrier1 depot)
    (person_at p1 l1) 
    (person_at p2 l1)
    (person_at p3 l1) 
    (person_at p4 l2)
    (person_at p5 l2) 
    (person_at p6 l3)
    (crate_at c1 depot) 
    (crate_at c2 depot) 
    (crate_at c3 depot) 
    (crate_at c4 depot) 
    (crate_at c5 depot) 
    (crate_at c6 depot) 
    (contain c1 medicine) 
    (contain c2 food) 
    (contain c3 beverage) 
    (contain c4 medicine) 
    (contain c5 food) 
    (contain c6 beverage)
    (available c1) 
    (available c2)
    (available c3) 
    (available c4)
    (available c5) 
    (available c6)
    (need p1 food)
    (need p1 beverage)
    (need p3 medicine)
    (need p4 food)
    (need p5 medicine)
    (need p6 beverage)
    (have p1 medicine) 
    (have p2 food) 
    (have p3 beverage)
    (= (capacity carrier1) 4)
  )

  (:goal
    (and (have p1 food) (have p1 beverage) (have p3 medicine) (have p4 food) (have p5 medicine) (have p6 beverage))
  )
)


; set instance robot1 robot

; set instance p1 person
; set instance p2 person
; set instance p3 person
; set instance p4 person
; set instance p5 person
; set instance p6 person

; set instance c1 crate
; set instance c2 crate
; set instance c3 crate
; set instance c4 crate
; set instance c5 crate
; set instance c6 crate

; set instance depot location
; set instance l1 location
; set instance l2 location
; set instance l3 location

; set instance medicine content
; set instance food content
; set instance beverage content

; set instance carrier1 carrier


; set predicate (robot_at robot1 depot)
; set predicate (free robot1)
        
; set predicate (carrier_at carrier1 depot)
        
; set predicate (person_at p1 l1) 
; set predicate (person_at p2 l1)
; set predicate (person_at p3 l1) 
; set predicate (person_at p4 l2)
; set predicate (person_at p5 l2) 
; set predicate (person_at p6 l3)

; set predicate (crate_at c1 depot) 
; set predicate (crate_at c2 depot) 
; set predicate (crate_at c3 depot) 
; set predicate (crate_at c4 depot) 
; set predicate (crate_at c5 depot) 
; set predicate (crate_at c6 depot) 
        
; set predicate (contain c1 medicine) 
; set predicate (contain c2 food) 
; set predicate (contain c3 beverage) 
; set predicate (contain c4 medicine) 
; set predicate (contain c5 food) 
; set predicate (contain c6 beverage)

; set predicate (available c1) 
; set predicate (available c2)
; set predicate (available c3) 
; set predicate (available c4)
; set predicate (available c5) 
; set predicate (available c6)

; set predicate (need p1 food)
; set predicate (need p1 beverage)
; set predicate (need p3 medicine)
; set predicate (need p4 food)
; set predicate (need p5 medicine)
; set predicate (need p6 beverage)

; set predicate (have p1 medicine) 
; set predicate (have p2 food) 
; set predicate (have p3 beverage)

; set function (= (capacity carrier1) 4)

; set goal (and (have p1 food) (have p1 beverage) (have p3 medicine) (have p4 food) (have p5 medicine) (have p6 beverage))