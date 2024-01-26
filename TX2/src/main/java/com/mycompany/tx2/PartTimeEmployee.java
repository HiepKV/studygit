/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.tx2;

/**
 *
 * @author PC
 */
public class PartTimeEmployee extends Employee {
    private int workingHour;

    public PartTimeEmployee() {
        super();
    }

    public PartTimeEmployee(int workingHour, String nmae, int paymentPerHour) {
        super(nmae, paymentPerHour);
        this.workingHour = workingHour;
    }
    
    
    public int getWorkingHour() {
        return workingHour;
    }

    public void setWorkingHour(int workingHour) {
        this.workingHour = workingHour;
    }
    @Override
    public int CalculateSalary() {
        //throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
        return paymentPerHour * workingHour;
    }

    @Override
    public String getName() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
    
}
