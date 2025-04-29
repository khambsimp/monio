# Radio Frequency Engineering
# Global Navigation Satellite System
This repository holds notes on gnss receivers, and technology which is utilized
to develop gnss capability within the monio system. Perhaps as a module add on or capability of the Computer.

# Global Positioning System
The Global Positiing System is the United States's  Global navigation system
# L1 Civilian
The L1 band is the original Civilian band and consists of 24 Satellites with their own Pseudo Random number generated code. A Ground station. And User Equipment in the form of Receivers. The Satellites communicate over the L1 Band at 1.57542 GHz.
# GPS System Satellite Architecture
L1 Band at 1.57542 GHz.
## Signal Generation block
50 bits per second nav message is repeated 20 times to produce a 1000 bits per second stream. Signal is spread by a C/A code with a length of 1023 chirps (chirps per second) this has the pseudorandom code embedded within it. this gives a baseband signal of 1.023 megabits per second. 43 dB processing gain is needed to resolve a signal well below the thermal noise level. The unique pseudorandom code of the satellite has excellent auto- and cross-correlation properties,  it can be used in code division multiple access systems.  Baseband signal (1.023 megabits per second (Mbps)) is modulated with binary phase-shift keying and unconverted to the L1 band for transmission.

# GNSS System Reciever Architecture
Receiver needs 4 Satellites in view to gain a reliable lock, that is for 3-D Positioning, and time. The RF-Front End consists of the Antenna cable received, then amplifies the weak signal with a low-noise-amplifier, then downconverts it to a low frequency around 4 MHz. Mixing (the multiplexer) with the local oscillator (reference oscilator is a temperature compensated crystal oscillator TCXO) . The resulting analog Intermediate frequency signal is converted to a digital intermediate frequency by the adc the result of the ADc is the I and Q file.  
The GNSS System components usually consist of an antenna, an RF cable (dma), a passive hybrid coupler, muxifier, low noise amplifier, bandpass filter, and then a receiver. The RF front-end and receiver are connected to a computer, or a pseudorange downconverter for transmission over a network.

# GNSS Software Defined Radio
To increase the number of experiments and versatility of our own gnss receiver we explore the theory of software defined radios to determine how to develop a system which is effective in its use of the received oncoming signal. And cost effective in the manner that it derives a final solution, in a way that can utilized by a minicomputer. The Hardware defined below should work with GNSS-SDR.

## Mixed Signal RF-Front-End Integrated Circuits for Software GPS receivers
[Analog Devices Mar 22 2007](https://www.analog.com/en/resources/technical-articles/rf-frontend-ic-simplifies-software-gps-receiver.html)

Example given MAX2741

Code Division Multiple Access (CDMA)
ICDMA is a spread spectrum technique
Each user is assigned a unique spreading code to separate the signal from other users.

## Acquisition
As a Code Division Multiple Access System the receiver uses code aquistion for coarse-code alignment, and code-phase tracking for fine alignment. Each satellite has a unique C/A code aquisition and code phase tracking mean the receiver has the information it needs to demodulate the the satellites parameters. The received signal requires code-phase tracking to compensate for the doppler effect of satellite to reveiver. 

### Serial Search
Suitable for a circuit, integrated circuit, application specific integrated circuit, field programmable 
gate array, due to logic architecture.
Received signal is first downconverted to in-phase quadrature (I and Q)
(Post-correlators) I-Q correlators then correlate the I and Q baseband signals with the locally 
generated PRN sequence.
This is the correlation function you are familiar with.
Once the correlation function meets a threshold value the reciever proceeds into tracking mode.
### Frequency Domain parallel code-phase aquisition
Low Computational complexity makes this an algorithmic implementation.
*General Philosophy*
Conduct a Fast Fourier Transform of the Pseudorandom number code, then once in the frequency domain, the code phase information is already present, therefore only the doppler frequency offser needs to be taken into account.
*Implementation*
Signal is multiplied (muxified)
Then these are combined into a Fast Fourier Transform.
This is multiplied by the the symmetric complex conjugate of the PRN code's Fast Fourier Transform, note these can even be stored as data beforehand.
The Fast Fourier Transform of the signal received and of the complex conjugate of the presdorandom generator are multiplplied, and fed through an inverse fourier transform block and converted by squaring to a magnitude which once it reaches a specific threshold the receiver reverts to tracking mode.
## Tracking
### Overview
















# GNSS Band
## GPS System (United States)
## GNSS L1 Band for Simplicity

# GNSS System Components
## Antenna
ALA.01 GPS/GALILEO Active Loop Antenna 45*10*2.3mm, 95mm Ø1.13, I-PEX MHF® I (U.FL)
Price
$21.87 Digikey
[Digikey Store](https://www.digikey.com/en/products/detail/taoglas-limited/ALA.01.07.0095A/2332641?curr=usd&utm_campaign=buynow&utm_medium=aggregator&utm_source=octopart)
## RF Cable (DMA)
## Hybrid Coupler
(TAOGLAS)[https://www.taoglas.com/product/hc125-a-low-profile-hybrid-coupler-for-multiband-gnss/]
## Low Noise Amplifier
[MAX2670EVKIT](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max2670evkit.html#eb-overview)
[SKY55951-11](https://www.skyworksinc.com/en/Products/Front-end-Modules/SKY55951-11)
Price:
$91.99 Mouser
[MAX2670EVKIT](https://www.mouser.com/ProductDetail/Analog-Devices-Maxim-Integrated/MAX2670EVKIT?qs=QjFvEcVG8GQViUuhfgeFLA%3D%3D&srsltid=AfmBOorAy8grynEewPvxviiSV_ts3gEyHWkQZiosVM5NVFhr5TutHno3)
## Muxifier
## Reciever
### Analog Devices
[MAX2754EVKIT+](https://www.analog.com/en/resources/evaluation-hardware-and-software/evaluation-boards-kits/max2741evkit.html#eb-overview)
Price:
$195.65
[MAX2754EVKIT+ Digikey](https://www.digikey.com/en/products/detail/analog-devices-inc-maxim-integrated/MAX2754EVKIT-/2349284?gclsrc=aw.ds&&utm_adgroup=&utm_source=google&utm_medium=cpc&utm_campaign=PMax%20Shopping_Product_Low%20ROAS%20Categories&utm_term=&utm_content=&utm_id=go_cmp-20243063506_adg-_ad-__dev-c_ext-_prd-2349284_sig-Cj0KCQjwzrzABhD8ARIsANlSWNOojj9gr2Dv9ADoL1ZUZ9YoozqONmMcOwzkLTqO363jreuBHLuF92AaAhtVEALw_wcB&gad_source=1&gbraid=0AAAAADrbLljzMiwv25wy_h8lnatg4Q1qr&gclid=Cj0KCQjwzrzABhD8ARIsANlSWNOojj9gr2Dv9ADoL1ZUZ9YoozqONmMcOwzkLTqO363jreuBHLuF92AaAhtVEALw_wcB)
### Ettus Research

## Computer

# Articles
[RF Front-End IC Simplifies Software GPS Receiver](https://www.analog.com/en/resources/technical-articles/rf-frontend-ic-simplifies-software-gps-receiver.html)
