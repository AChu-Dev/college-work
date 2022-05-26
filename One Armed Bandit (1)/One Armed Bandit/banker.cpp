#pragma once;
#include <iostream>
#include <iomanip>
#include <windows.h>
#include <string>
#include "Banker.h"
 
using namespace std;

Banker::Banker() 
{
	curr = 0;
	jPot = 0;
}


float Banker::input_Money(float curr) {
	ten_pence = 0, twenty_pence = 0, fifty_pence = 0, pound = 0;
	cout << "Please use 0 as empty lines, and only input numbers" << endl << endl;
	cout << "How many 10ps are you inputting? ";
	cin >> ten_pence;
	cout << endl << "How many 20ps are you inputting? ";
	cin >> twenty_pence;
	cout << endl << "How many 50ps are you inputting? ";
	cin >> fifty_pence;
	cout << endl << "How many Pounds are you inputting? ";
	cin >> pound;
	
	new_curr = curr + (ten_pence * 0.10) + (twenty_pence * 0.20) + (fifty_pence * 0.50) + pound;
	if (new_curr < 0) {
		cout << "You have inputted incorrectly, Money will not be changed"<< endl;
	}
	else {
		curr = new_curr;
	}
	cout << "Your new Money Value is: "<<curr;
	return curr;
}


float Banker::output_Money(float curr) {
	cout << "I will now calculate your outputted money: ";
	curr = curr * 10;
	cout << std::fixed << std::setprecision(0) << curr << " * 10p's Have Been Outputted";
	curr = 0;
	return curr;
}