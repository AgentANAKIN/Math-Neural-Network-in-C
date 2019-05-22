// This neural network was originally written in Python (https://www.sololearn.com/learn/744/?ref=app). I converted it to C to deepen my understanding of both languages, as well as of neural networks.



#include <stdlib.h> 
#include <stdio.h>

int main() {


 
// Seed the pseudo-random number generator with the Process ID. No, this is not the best method. But, it works for this exercise.
srand((unsigned int)getpid()); 



// Generate random weights.
double weight0 = 2*(((double)rand())/RAND_MAX)-1;
double weight1 = 2*(((double)rand())/RAND_MAX)-1;
printf("weight0 %f weight1 %f\n", weight0, weight1);



// Provide training data.
int inputs[4][2] = {{2,3}, {1,1}, {5,2}, {12,3}};
int outputs[4] = {10, 4, 14, 30};



// Think!
double think(double x, double y){
    return((x * weight0) + (y * weight1));
}



// Train the model.
int i, j;
double error, adjustment;
void train() {
    for (i=0; i<300; i++){
        for (j=0; j<4; j++){
            error = (outputs[j] - think(inputs[j][0],inputs[j][1]));
            adjustment = (.01 * error * inputs[j][0]);
            weight0 += adjustment;
            adjustment = (.01 * error * inputs[j][1]);
            weight1 += adjustment;
            }
        if (i % 10 == 0) {
        printf("i %i error %f\nweight0 %f weight1 %f\n", i, error, weight0, weight1);
        }
    }
}
train();



// Test the model with new inputs.
printf("test %f\n", think(15,2));

    return 0;
}
