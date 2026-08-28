class User:
    def login(self):
        print("every user must be login")
class Manager(User):
    def manage_users(self):
        print("manager can manage the users")

m=Manager()
m.login()
m.manage_users()

class Father:
    def dance(self):
        print("dancing")
class Mother:
    def cook(self):
        print("cooking")
class Child(Father,Mother):
    def play(self):
        print("playing")
c=Child()
c.dance()
c.play()
c.cook()

# Multi-level
class animal:
    def eat(self):
        print("eating")
class dog(animal):
    def bark(self):
        print("barking")
class babydog(dog):
    def cry(self):
        print("crying")
b=babydog()
b.cry()
b.bark()
b.eat()
# Hierarchical
class Vehicle:
    def fuel_type(self):
        print("Uses fuel or battery")

class Car(Vehicle):
    def drive(self):
        print("Driving the car")

class Bike(Vehicle):
    def ride(self):
        print("Riding the bike")
s=Car()
s.fuel_type()
s.drive()
s1=Bike()
s1.ride()
s1.fuel_type()
Hybrid 
class A:
    def m1(self):
        print("m1 method in A class")
class B(A):
    def m2(self):
        print("m2 method in B class")
class C(A):
    def m3(self):
        print("m3 method in C class")
class D(B,C):
    def m4(self):
        print("m4 method in D class")

d=D()
d.m4()
d.m2()

# super()
class Parent:
    def __init__(self):
        print("Parent constructor called")

class Child(Parent):
    def __init__(self):
        super().__init__()  
        print("Child constructor called")

c = Child()

