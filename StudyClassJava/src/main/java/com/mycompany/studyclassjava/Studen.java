/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.studyclassjava;
/**
 *
 * @author PC
 */
public class Studen {
        public int Id, Age;
        public String Email;
        private String Name;
        
    public Studen(){
    }
    public Studen(int Id, int Age, String Name, String Email) {
        this.Id = Id;
        this.Age = Age;
        this.Name = Name;
        this.Email = Email;
    }

    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }

    public int getAge() {
        return Age;
    }

    public void setAge(int Age) {
        this.Age = Age;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public String getEmail() {
        return Email;
    }

    public void setEmail(String Email) {
        this.Email = Email;
    }
    @Override
    public String toString(){
        return "ID : "+ Id +"\t Name : "+ Name +"\t Email : "+ Email+"\t Age :" + Age;
    }
}

