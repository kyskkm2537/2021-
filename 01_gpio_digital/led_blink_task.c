#include <wiringPi.h>
#define RED_LED 7
#define YELLOW_LED 26
#define GREEN_LED 12
int main (void)
{
  wiringPiSetup () ;
  pinMode (RED_LED, OUTPUT) ;
  pinMode (YELLOW_LED, OUTPUT) ;
  pinMode (GREEN_LED, OUTPUT) ;

  for (int i=0;i<5;i++)
  {
    digitalWrite (RED_LED, HIGH) ; delay (2000) ;
    digitalWrite (RED_LED,  LOW) ;
    digitalWrite (YELLOW_LED, HIGH) ; delay (2000) ;
    digitalWrite (YELLOW_LED,  LOW) ;
    digitalWrite (GREEN_LED, HIGH) ; delay (2000) ;
    digitalWrite (GREEN_LED,  LOW) ;
  }
  return 0 ;
}