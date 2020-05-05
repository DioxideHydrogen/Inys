#include <Ethernet.h>
#include <MySQL_Connection.h>
#include <MySQL_Cursor.h>
#include <SPI.h>

// Display 16x2 Configurações
#include <LiquidCrystal.h>

const byte rs = 9;
const byte en = 8;
const byte d4 = 7;
const byte d5 = 6;
const byte d6 = 5;
const byte d7 = 4; 

const byte vermelhoTemp= 3;
const byte verdeTemp = 2;

const byte buzzerTemp = A2;
float seno;
int frequencia;

LiquidCrystal lcd(rs,en,d4,d5,d6,d7);

// DHT11 Configurações
#define LM35 A8
int leitura;
float temperatura;

char sentenca[128];
char valortemp[10];
char valorldr[10];

byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
byte ip[] = {10,139,185,71};
byte subnet[] = {255,255,255,0}; 
byte gateway[] = {10,139,185,254};

IPAddress server_addr(10,139,185,60);
char user[] = "root";
char password[] = "123";

char ATUALIZAR_SENSORES[] = "UPDATE alexa_sensores SET temp = %s, ldr = %s WHERE id = 1";
char BANCODEDADOS[] = "USE alexa_db";

#define salaPINO A4

char sala[] = "SELECT * FROM alexa_eletronicos";

#define quartoPINO A5

char quarto[] = "SELECT quarto FROM alexa_eletronicos";

#define cozinhaPINO 3

char cozinha[] = "SELECT cozinha FROM alexa_eletronicos";

#define banheiroPINO 4

char banheiro[] = "SELECT banheiro FROM alexa_eletronicos";
EthernetClient client;
MySQL_Connection conn((Client *)&client);
MySQL_Cursor cur = MySQL_Cursor(&conn);
#define LDR A9
int ldrPin;

#define rele1 A4

#define rele2 A5

void setup() {
   pinMode(vermelhoTemp, OUTPUT);
   pinMode(verdeTemp, OUTPUT);
   pinMode(buzzerTemp, OUTPUT);
   pinMode(rele1, OUTPUT);
   pinMode(rele2, OUTPUT);
   pinMode(salaPINO, OUTPUT);
   pinMode(quartoPINO, OUTPUT);
   lcd.begin(16,2);
   lcd.setCursor(0,0);
   lcd.print("Celsius: "); 
   lcd.setCursor(0,1);
   lcd.print("Umidade: ");
   Serial.begin(9600);
   while (!Serial); 
    Ethernet.begin(mac, ip, subnet, gateway);
    Serial.println("Ativando IP do Arduino");
    delay(1000);   // espera por 1 segundo
    Serial.println("Conectando...");
    Serial.println(Ethernet.localIP());
    if (conn.connect(server_addr, 3306, user, password)){
      delay(1000);
      Serial.println("Conexão com o MySQL estabelecida");
      MySQL_Cursor *cur_mem = new MySQL_Cursor(&conn);
      cur_mem->execute(BANCODEDADOS);
      delete cur_mem;
   }
   else{
      Serial.println("A conexão falhou");
      conn.close();
   }
  }


void loop() {
   long salaValor, cozinhaValor, quartoValor, banheiroValor = 0;
   row_values *row = NULL;
   leitura = analogRead(LM35);
   temperatura = (float(analogRead(LM35))*5/(1023))/0.01;
   dtostrf(temperatura, 4, 1, valortemp);
   lcd.setCursor(9,0);
   lcd.print(temperatura);
   lcd.print(char(223));
   lcd.print('C');
   if(temperatura > 35){
      digitalWrite(verdeTemp,LOW);
      digitalWrite(vermelhoTemp, HIGH);      
      for(int x=0;x<180;x++){
        //converte graus para radiando e depois obtém o valor do seno
        seno=(sin(x*3.1416/180));
        //gera uma frequência a partir do valor do seno
        frequencia = 2000+(int(seno*1000));
        tone(buzzerTemp,frequencia);
        delay(2);
      }
    } else {
      digitalWrite(verdeTemp, HIGH);
      digitalWrite(vermelhoTemp, LOW);
      noTone(buzzerTemp);
    }
   
   ldrPin = analogRead(LDR);
   dtostrf(ldrPin, 4, 1, valorldr);
   sprintf(sentenca, ATUALIZAR_SENSORES, valortemp, valorldr);
   lcd.setCursor(9,1);
   lcd.print(ldrPin);
   //Serial.println(sentenca);
   MySQL_Cursor *cur_mem = new MySQL_Cursor(&conn);
   cur_mem->execute(sentenca);
   delete cur_mem;
   
   MySQL_Cursor *cur_select = new MySQL_Cursor(&conn); 
   cur_select->execute(sala);
   column_names *columns = cur_select->get_columns();
   
   do {
    row = cur_select->get_next_row();
    if (row != NULL) {
      salaValor = atol(row->values[1]);
      quartoValor = atol(row->values[2]);
      cozinhaValor = atol(row->values[3]);
      banheiroValor = atol(row->values[4]);
    }
  } while (row != NULL);
   delete cur_select;
   Serial.print("SALA = ");
   Serial.println(salaValor);

   Serial.print("QUARTO = ");
   Serial.println(quartoValor);

   Serial.print("COZINHA = ");
   Serial.println(cozinhaValor);

   Serial.print("BANHEIRO = ");
   Serial.println(banheiroValor);
   
   if(salaValor == 0){
    digitalWrite(salaPINO, LOW);
   } else {
    digitalWrite(salaPINO, HIGH);
   }
   if(quartoValor == 0){
    digitalWrite(quartoPINO, LOW);
   } else {
    digitalWrite(quartoPINO, HIGH);
   }
   
   delay(1000);

}
