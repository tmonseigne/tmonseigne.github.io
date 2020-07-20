---
layout: post
title: Mémo Arithmétique
date: 2017-05-04
description: Mémo Arithmétique
img: theme/Memo-Theme.png # Add image post (optional)
tags: [Mémos]
author: Thibaut Monseigne # Add name author (optional)
---

<script language="JavaScript">
	Liste_Premier = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569, 571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631, 641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701, 709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773, 787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857, 859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937, 941, 947, 953, 967, 971, 977, 983, 991, 997];

	//Ids
	var id_NbP_Is, id_NbP_True, id_NbP_False,
		id_NbP_Decompo, id_NbP_Decompo_Res,
		id_NbP_Facto,id_NbP_Facto_Res,
		id_NbP_Frac_Num,id_NbP_Frac_Den,id_NbP_Frac_Res,
		id_PGCD_a, id_PGCD_b, id_PGCD_Res,
		id_PPCM_a, id_PPCM_b, id_PPCM_Res,
		id_Fact, id_Fact_Res,
		id_Fibo, id_Fibo_Res;

	function EstPremier(n){
		// Si inférieur à 1000 pas la peine de calucler j'ai une liste
		if (n < 1009) {
			if(Liste_Premier.indexOf(n)!=-1) { return true; }
			return false;
		}
		var max = Math.sqrt(n);
		for (var i = 2; i <= max; i++){
			if (n%i == 0){ return false; }
		}
		return true;
	}

	function DecompositonEnNombrePremier(n)
	{
		var res = [];
		var max = Math.sqrt(n);
		if (EstPremier(n)){
			res.push(n);
		} else {
			var i = 2;
			while (i <= max) {
				if (n%i == 0){
					res.push(i);
					n /= i;
					max = Math.sqrt(n);
				} else { i++; }
			}
			if (n!=1){ res.push(n); }
		}
		return res;
	}

	function PGCD(a,b)
	{
		/*
		while(a*b != 0){
			if (a > b)	a = a - b;
			else b = b - a;
		}
		if (a == 0){ return b; }
		return a;
		*/
		return (b==0) ? a : PGCD(b,a%b);
	}

	function PPCM(a,b)
	{
		return ((a*b) / PGCD(a,b));
	}

	function Factoriel(n)
	{
		var res = 1;
		for (var i = 2; i <= n; i++) {
			res *= i;
		}
		return res;
	}

	function Fibonacci(n)
	{
		if (n == 0)	{return 0;}
		if (n == 1)	{return 1;}
		return Fibonacci(n - 1) + Fibonacci(n - 2);
	}

	function EstPremierHandler()
	{
		var n = parseInt(id_NbP_Is.value);
		id_NbP_True.style.display = 'none';
		id_NbP_False.style.display = 'none';
		if(EstPremier(n)){
			id_NbP_True.style.display = 'initial';
			id_NbP_False.style.display = 'none';
		}
		else{
			id_NbP_True.style.display = 'none';
			id_NbP_False.style.display = 'initial';
		}
	}

	function DecompositonEnNombrePremierHandler()
	{
		/*
		var n = parseInt(id_NbP_Decompo.value);
		var res = DecompositonEnNombrePremier(n);
		var text = res.join("x");
		id_NbP_Decompo_Res.innerHTML = text;
		*/
		id_NbP_Decompo_Res.innerHTML = DecompositonEnNombrePremier(parseInt(id_NbP_Decompo.value)).join("x");
	}

	function FactorisationHandler()
	{
		var val = id_NbP_Facto.value;
		var plus_split = val.split("+");
		var D_val = [];
		for (var i =0; i < plus_split.length;i++){
			D_val.push(DecompositonEnNombrePremier(parseInt(plus_split[i])));
		}
		var fact = 1;
		var i = 0;
		while (i < D_val[0].length){
			var idxs = [i];
			for (var j = 1; j <D_val.length; j++){
				idxs.push(D_val[j].indexOf(D_val[0][i]));
			}
			if(idxs.indexOf(-1)==-1){
				fact *= D_val[0][i];
				for (var j = 0; j <D_val.length; j++){
					D_val[j].splice(idxs[j], 1);
				}
			}
			else {
				i++
			}
		}
		for (var j = 0; j <D_val.length; j++){
			D_val[j] = D_val[j].length!=0 ? D_val[j].reduce( (x,y) => x * y ) : 1;
		}
		var text = fact==1 ? D_val.join("+") : fact.toString() + "x("+D_val.join("+")+ ")";
		id_NbP_Facto_Res.innerHTML = text;
	}

	function ReductionHandler(){
		var a = parseInt(id_NbP_Frac_Num.value);
		var b = parseInt(id_NbP_Frac_Den.value);
		var D_a = DecompositonEnNombrePremier(a);
		var D_b = DecompositonEnNombrePremier(b);
		var i = 0
		while (i < D_a.length){
			idx = D_b.indexOf(D_a[i])
			if (idx != -1){
				D_a.splice(i, 1);
				D_b.splice(idx, 1);
			}
			else {
				i++
			}
		}
		new_a = (D_a.length != 0) ? D_a.reduce( (x,y) => x * y ) : 1;
		new_b = (D_b.length != 0) ? D_b.reduce( (x,y) => x * y ) : 1;
		id_NbP_Frac_Res.innerHTML = (new_b!=1) ? new_a+"/"+new_b : new_a;
	}

	function PGCDHandler(){
		var a = parseInt(id_PGCD_a.value);
		var b = parseInt(id_PGCD_b.value);
		id_PGCD_Res.innerHTML = "PGCD("+a.toString()+","+b.toString()+") = " + PGCD(a,b).toString();
	}

	function PPCMHandler(){
		var a = parseInt(id_PPCM_a.value);
		var b = parseInt(id_PPCM_b.value);
		id_PPCM_Res.innerHTML = "PPCM("+a.toString()+","+b.toString()+") = " + PPCM(a,b).toString();
	}

	function FactorielHandler(){
		id_Fact_Res.innerHTML = Factoriel(parseInt(id_Fact.value)).toString();
	}

	function FibonacciHandler(){
		id_Fibo_Res.innerHTML = Fibonacci(parseInt(id_Fibo.value)).toString();
	}

	function init(){
		EstPremierHandler();
		DecompositonEnNombrePremierHandler();
		FactorisationHandler();
		ReductionHandler();
		PGCDHandler();
		PPCMHandler();
		FactorielHandler();
		FibonacciHandler();
	}

	window.onload = function () {
		// Affectation
		id_NbP_Is = document.getElementById('NbP_Is');
		id_NbP_True = document.getElementById('NbP_True');
		id_NbP_False = document.getElementById('NbP_False');

		id_NbP_Decompo = document.getElementById('NbP_Decompo');
		id_NbP_Decompo_Res = document.getElementById('NbP_Decompo_Res');

		id_NbP_Facto = document.getElementById('NbP_Facto');
		id_NbP_Facto_Res = document.getElementById('NbP_Facto_Res');		

		id_NbP_Frac_Num = document.getElementById('NbP_Frac_Num');
		id_NbP_Frac_Den = document.getElementById('NbP_Frac_Den');		
		id_NbP_Frac_Res = document.getElementById('NbP_Frac_Res');		

		id_PGCD_a = document.getElementById('PGCD_a');
		id_PGCD_b = document.getElementById('PGCD_b');
		id_PGCD_Res = document.getElementById('PGCD_Res');

		id_PPCM_a = document.getElementById('PPCM_a');
		id_PPCM_b = document.getElementById('PPCM_b');
		id_PPCM_Res = document.getElementById('PPCM_Res');

		id_Fact = document.getElementById('Fact');
		id_Fact_Res = document.getElementById('Fact_Res');
		id_Fibo = document.getElementById('Fibo');
		id_Fibo_Res = document.getElementById('Fibo_Res');

		//Handler
		id_NbP_Is.onchange = EstPremierHandler;
		id_NbP_Decompo.onchange = DecompositonEnNombrePremierHandler;
		id_NbP_Facto.onchange = FactorisationHandler;
		id_NbP_Frac_Num.onchange = ReductionHandler;
		id_NbP_Frac_Den.onchange = ReductionHandler;
		id_PGCD_a.onchange = PGCDHandler;
		id_PGCD_b.onchange = PGCDHandler;
		id_PPCM_a.onchange = PPCMHandler;
		id_PPCM_b.onchange = PPCMHandler;
		id_Fact.onchange = FactorielHandler;
		id_Fibo.onchange = FibonacciHandler;

		init();
	}
</script>

## Définitions

**Nombres Premiers** : Un nombre premier est un entier naturel qui admet exactement deux diviseurs distincts entiers et positifs (qui sont alors 1 et lui-même). Ainsi, 1 n'est pas premier, car il n'a qu'un seul diviseur entier positif ; 0 non plus, car il est divisible par tous les entiers positifs.

**PGCD** : Le plus grand commun diviseur, abrégé en général PGCD, de deux nombres entiers naturels non nuls est le plus grand entier qui divise simultanément ces deux entiers.

**PPCM** : Le plus petit commun multiple, abrégé en général PPCM, de deux nombres entiers non nuls est le plus petit entier strictement positif qui soit à la fois multiple de ces deux nombres.

**Factoriel** : La factorielle d'un entier naturel n est le produit des nombres entiers strictement positifs inférieurs ou égaux à n. Cette opération est notée avec un point d'exclamation : n !

**Fibonacci** : La suite de Fibonacci est une suite d'entiers dans laquelle chaque terme est la somme des deux termes qui le précèdent. Elle commence généralement par les termes 0 et 1 (parfois 1 et 1) et ses premiers termes sont : 0, 1, 1, 2, 3, 5, 8, 13, 21, etc.

## Exemples

|:----|:----|:----|:----|
|Savoir si un nombre est premier : |<input type="number" style="width: 5em;" min="0" id="NbP_Is" value="2">|&nbsp;=>&nbsp;|<font size="6"><span style="color:green" id="NbP_True">&#10004;</span><span style="color:red" id="NbP_False">&#10008;</span></font>|
|Décomposition en Nombre premier : |<input type="number" min="0" style="width: 5em;" id="NbP_Decompo" value="2">|&nbsp;=>&nbsp;|<span id="NbP_Decompo_Res"></span>|
|Factorisation (uniquement additions) : |<input type="text" name="factorisation" size="40" id="NbP_Facto" value="52+38+56+94">|&nbsp;=>&nbsp;|<span id="NbP_Facto_Res"></span>|
|Réduction de Fraction : |<input type="number" style="width: 5em;" min="0" id="NbP_Frac_Num" value="1"> &nbsp;/&nbsp; <input type="number" style="width: 5em;" min="1" id="NbP_Frac_Den" value="2">|&nbsp;=>&nbsp;|<span id="NbP_Frac_Res"></span>|
|PGCD : |a : <input type="number" style="width: 5em;" min="0" id="PGCD_a" value="1">, b : <input type="number" style="width: 5em;" min="0" id="PGCD_b" value="2">|&nbsp;=>&nbsp;|<span id="PGCD_Res"></span>|
|PPCM : |a : <input type="number" style="width: 5em;" min="0" id="PPCM_a" value="1">, b : <input type="number" style="width: 5em;" min="0" id="PPCM_b" value="2">|&nbsp;=>&nbsp;|<span id="PPCM_Res"></span>|
|Factoriel : |<input type="number" style="width: 5em;" min="0" id="Fact" value="1">|&nbsp;=>&nbsp;|<span id="Fact_Res"></span>|
|Fibonacci : |<input type="number" style="width: 5em;" min="0" id="Fibo" value="1">|&nbsp;=>&nbsp;|<span id="Fibo_Res"></span>|
