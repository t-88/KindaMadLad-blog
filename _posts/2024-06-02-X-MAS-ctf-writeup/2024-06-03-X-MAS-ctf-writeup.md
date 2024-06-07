---
layout: post
title:  "X-MAS ctf writeup"
date:   2024-06-03 11:20:00 +0100
tags: writup ctf
---

## Emulation
# Emu 2.0

### description: 
> Hey! We have found this old cartridge under a desk in the library of Lapland. It appears to be for a system called "Emu 2.0", made back in 1978. These systems don't get produced anymore, and we can't seem to find anyone that owns one. Thankfully we have the documentation for it, so maybe we can use it to write an emulator and see what this ROM does?   

### files: 
- [Emu 2.0 Documentation]({{site.baseurl}}{%link assets/2024-06-02-X-MAS-ctf-writeup/emu2.0/Emu 2.0 Documentation.pdf%})   
- [rom]({{site.baseurl}}{%link assets/2024-06-02-X-MAS-ctf-writeup/emu2.0/rom%})

### solution
this challange requires you to write a emulator for emu2.0 cpu    
writing emulators is all about **reading the docs**, and thats all you gonna need to solve this challange, ofc with some basic understanding of bit manipulation for overflow cases and binary operations (or, and , xor...)    
        
after some writing and rewriting, i got the emulator to work, pretty simple challange

- [sol.py]({{site.baseurl}}{%link assets/2024-06-02-X-MAS-ctf-writeup/emu2.0/sol.py%})   
- <details>  <summary>flag </summary> X-MAS{S4nt4_U5e5_An_Emu_2.0_M4ch1n3}  </details>

<br>
<br>
<br>
<br>
    
    
# Chip9
> Hardware is the nuts and bolts of the entire computer system. A cassette deck which loads programs into a home computer is part of the hardware. So is the home television set if it is used to display the output from the computer.   
The keyboard, the memory, printers; just about anything solid to do with a computer comes under the definition of hardware.    
Software refers to the programs that make the computer useful. Nominally the term includes the medium upon which the programs are recorded, be it paper tape, casette tape, a disc of tape, punched cards or even a book of software.

### files:
- [chip9 docs]({{site.baseurl}}{%link assets/2024-06-02-X-MAS-ctf-writeup/chip9/CHIP9 Manual.pdf%})   
- [bootrom]({{site.baseurl}}{%link assets/2024-06-02-X-MAS-ctf-writeup/chip9/bootrom%})
- [rom]({{site.baseurl}}{%link assets/2024-06-02-X-MAS-ctf-writeup/chip9/rom%})

### notes
i didnt solve it, i tried solving it with python twice for two days then i gave up. i dont think its worth it to solve hard emulation challanges in short ctfs  (skill issue).    
i have few notes for future me:
- dont use python for in depth emulation challanges, i reached a point where i am waiting 2 mins to get a unsupported op (my main idea was to run my emulator and not support all instruction so when my program finds a unsupported instruction it would stop)
- in python there is a big diff between ```[[0] * 128] * 64``` and ```[[0] * 128 for i in range(64)]``` use the second

