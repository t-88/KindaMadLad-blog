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