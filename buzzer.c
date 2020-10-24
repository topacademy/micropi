/*
MUSICAL_BUZZER  Plays notes from 'close encounters' movie theme once
Also supplies all required frequencies for other notes
Very much 'bare metal' code using microsecond delays to create frequency
*/

#define buzzer 12

void tone(int pitch, int len)
{
	long n;
	unsigned long tt;
	pinMode(buzzer, OUTPUT);
  
	switch(pitch)		//note		Frequency
	{
	case 21: 
		tt=1432;		// F		349.23
		break;
	case 22: 
		tt=1351;		// F#		369.99 
		break;
	case 23: 
		tt=1276;		// G		391.99 
		break;
	case 24: 
		tt=1204;		// G#		415.31
		break;
	case 25: 
		tt=1136;		// A4		440.00 
		break;
	case 26: 
		tt=1073;		// A#		466.16 
		break;
	case 27: 
		tt=1012;		// B		493.88 
		break;
	case 28: 
		tt=956;			// C		523.25 
		break;
	case 29: 
		tt=902;			// C#		554.36 
		break;
	case 30: 
		tt=851; 		// D		587.32
		break;
	case 31: 
		tt=804;			// D#		622.25 
		break;
	case 32: 
		tt=758;			// E		659.25 
		break;
	case 33: 
		tt=716;			// F		698.45 
		break;
	case 34: 
		tt=676;			// F#		739.99 
		break;
	case 35: 
		tt=638;			// G		783.99 
		break;
	case 36: 
		tt=602; 		// G#		830.61
		break;
	case 37: 
		tt=568; 		// A5		880.00
		break;
	case 38: 
		tt=536; 		// A#		932.32
		break;
	case 39: 
		tt=506; 		// B5		987.76
		break;
	default: 
		tt=284; 		// C6		1760.00
		break;
	}
  
	n = len * 100000 / tt;
	tt-=12;		        				//Account for loop overheads
	while(n>0)
	{
		digitalWrite(buzzer, HIGH);
		delayMicroseconds(tt);      	//delay
		digitalWrite(buzzer, LOW);
		delayMicroseconds(tt);      	//delay
		n--;                        	//loop takes about 12 cycles
	}
}

//Tasks which need to execute once when the program starts

void setup()
{
	tone(35,1);                     	//close encounters theme
	tone(37,1);
	tone(33,1);
	tone(21,1);
	tone(28,2);
}

//Main operating loop
void loop()
{

}

