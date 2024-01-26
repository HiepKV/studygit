/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.tx2;

/**
 *
 * @author PC
 */
public class FullTimeEmployee extends Employee{

    public FullTimeEmployee(String nmae, int paymentPerHour) {
        super(nmae, paymentPerHour);
    }

    public FullTimeEmployee() {
        super();
    }

    @Override
    public int CalculateSalary() {
        //throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
        return 8 * paymentPerHour;
    }

    @Override
    public String getName() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
    
}
