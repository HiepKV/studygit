/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.tx2;

/**
 *
 * @author PC
 */
public abstract class Employee implements IEmployee {
    private String nmae;
    public int paymentPerHour;

    public Employee() {
    }

    public Employee(String nmae, int paymentPerHour) {
        this.nmae = nmae;
        this.paymentPerHour = paymentPerHour;
    }

    public String getNmae() {
        return nmae;
    }

    public void setNmae(String nmae) {
        this.nmae = nmae;
    }

    public int getPaymentPerHour() {
        return paymentPerHour;
    }

    public void setPaymentPerHour(int paymentPerHour) {
        this.paymentPerHour = paymentPerHour;
    }
    
}
