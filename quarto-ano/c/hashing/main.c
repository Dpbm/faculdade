#include <stdio.h>
#include <stdint.h>
#include <assert.h>
#include <math.h>
#include <stdbool.h>

#define W 3
#define S (uint8_t)100
#define KEY (uint16_t)(pow(2,15) + pow(2,13) + pow(2,10) + pow(2,8))

uint16_t concat(uint8_t s, uint8_t x){
	uint16_t s_ext = (uint16_t)s;
	uint16_t x_ext = (uint16_t)x;
	s_ext <<= (uint16_t)8;
	return (uint16_t)(s_ext+x_ext);
}


uint16_t hash(uint16_t x){
	// Dummy hash function
	return x^KEY;
}

bool compare_left(uint16_t h, uint8_t w){
	assert(w >= 0 && w <= 16);
	uint8_t shift = (uint8_t)(16 - w);
	return (h >> shift) == 0;
}


int main(){
	assert(concat(1,1) == 257);	
	assert(concat(128,128) == 32896);

	assert(hash(KEY) == 0);
	assert(hash(KEY+1) == 1);

	assert(compare_left(0, 10));
	assert(!compare_left((uint16_t)32768, 3));
	assert(compare_left((uint16_t)4096, 3));

	uint8_t x = (uint8_t) 0;

	while(true){
		uint16_t c = concat(x,S);
		uint16_t h = hash(c);
		bool found = compare_left(h,W);
		printf("x=%d; s=%d; c=%d; h=%04x; found=%b\n", x, S, c, h, found);

		if(found) break;


		fflush(stdout);

		x++;
	}

	return 0;
}
