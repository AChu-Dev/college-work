#pragma once


class Banker {
public:
	Banker();
	float curr, jPot, new_curr;
	float input_Money(float x);
	float output_Money(float x);
	int pound, ten_pence, twenty_pence, fifty_pence, x;
};