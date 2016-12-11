# seccon2016-vigenere-writeup
Seccon 2016 Vigenere Writeup

The question was like following:

Vigenere
<br/>
k: ????????????<br/>
p: SECCON{???????????????????????????????????}<br/>
c: LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ<br/>
<br/>
k=key, p=plain, c=cipher, md5(p)=f528a6ab914c1ecf856a1d93103948fe<br/>
<br/>
|ABCDEFGHIJKLMNOPQRSTUVWXYZ{}<br/>
-+----------------------------<br/>
A|ABCDEFGHIJKLMNOPQRSTUVWXYZ{}<br/>
B|BCDEFGHIJKLMNOPQRSTUVWXYZ{}A<br/>
C|CDEFGHIJKLMNOPQRSTUVWXYZ{}AB<br/>
D|DEFGHIJKLMNOPQRSTUVWXYZ{}ABC<br/>
E|EFGHIJKLMNOPQRSTUVWXYZ{}ABCD<br/>
F|FGHIJKLMNOPQRSTUVWXYZ{}ABCDE<br/>
G|GHIJKLMNOPQRSTUVWXYZ{}ABCDEF<br/>
H|HIJKLMNOPQRSTUVWXYZ{}ABCDEFG<br/>
I|IJKLMNOPQRSTUVWXYZ{}ABCDEFGH<br/>
J|JKLMNOPQRSTUVWXYZ{}ABCDEFGHI<br/>
K|KLMNOPQRSTUVWXYZ{}ABCDEFGHIJ<br/>
L|LMNOPQRSTUVWXYZ{}ABCDEFGHIJK<br/>
M|MNOPQRSTUVWXYZ{}ABCDEFGHIJKL<br/>
N|NOPQRSTUVWXYZ{}ABCDEFGHIJKLM<br/>
O|OPQRSTUVWXYZ{}ABCDEFGHIJKLMN<br/>
P|PQRSTUVWXYZ{}ABCDEFGHIJKLMNO<br/>
Q|QRSTUVWXYZ{}ABCDEFGHIJKLMNOP<br/>
R|RSTUVWXYZ{}ABCDEFGHIJKLMNOPQ<br/>
S|STUVWXYZ{}ABCDEFGHIJKLMNOPQR<br/>
T|TUVWXYZ{}ABCDEFGHIJKLMNOPQRS<br/>
U|UVWXYZ{}ABCDEFGHIJKLMNOPQRST<br/>
V|VWXYZ{}ABCDEFGHIJKLMNOPQRSTU<br/>
W|WXYZ{}ABCDEFGHIJKLMNOPQRSTUV<br/>
X|XYZ{}ABCDEFGHIJKLMNOPQRSTUVW<br/>
Y|YZ{}ABCDEFGHIJKLMNOPQRSTUVWX<br/>
Z|Z{}ABCDEFGHIJKLMNOPQRSTUVWXY<br/>
{|{}ABCDEFGHIJKLMNOPQRSTUVWXYZ<br/>
}|}ABCDEFGHIJKLMNOPQRSTUVWXYZ{<br/>
<br/>
Vigenere cipher<br/>
https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher<br/>
<br/>
<br/>
First, we have to derive key to decrypt the ciphertext.
As given some of the plaintext is : <b>SECCON{</b> and <b>}</b>
So we derived the key from first 7 characters of ciphertext: <b>LMIG}RP</b>

The derived key is: VIGENERxxxxx
Since the algorithm is Vigenere, we guessed that the 8th character is <b>E</b> and the current key value is:
<b>VIGENERExxxx</b>

In Vigenere algorithm the key is repeated by the length of plaintext.
So we divided plaintext by 12 which is keys length.

key:    VIGENERExxxxVIGENERExxxxVIGENERExxxxVIGENER
cipher: LMIG}RPEDOEEWKJIQIWKJWMNDTSR}TFVUFWYOCBAJBQ
plain:  SECCON{AxxxxBCDEDEFGxxxxKLMNOPQRxxxxVWXYYZ}

We saw that the missing parts of plain text are relevant to neighbor characters. 
* In the first chunk the characters will be some sequence of A,B,C
* In the second chunk the characters will be some sequence of F,G,H,I,J,K,L
* In the third chunk the characters will be some sequence of Q,R,S,T,U,V,W

Since we have md5 of plaintext, we write a code that tries the md5 of following sequences to derive the key.

![alt tag](https://github.com/rustempasha/seccon2016-vigenere-writeup/blob/master/screenshot.png)

Flag is: <b>SECCON{ABABABCDEDEFGHIJJKLMNOPQRSTTUVWXYYZ}</b>
