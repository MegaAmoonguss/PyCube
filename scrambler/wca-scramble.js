// Default settings
var size=3;
var seqlen=30;
var numcub=1;
var mult=false;
var cubeorient=false;
var colorString = "yobwrg";  //In dlburf order. May use any colours in colorList below
 
// list of available colours
var colorList=new Array(
	'y', "yellow.jpg", "yellow",
	'b', "blue.jpg",   "blue",
	'r', "red.jpg",    "red",
	'w', "white.jpg",  "white",
	'g', "green.jpg",  "green",
	'o', "orange.jpg", "orange",
	'p', "purple.jpg", "purple",
	'0', "grey.jpg",   "grey"      // used for unrecognised letters, or when zero used.
);
 
var colors=new Array(); //stores colours used
var seq=new Array();	// move sequences
var posit = new Array();	// facelet array
var flat2posit;	//lookup table for drawing cube
var colorPerm = new Array(); //dlburf face colour permutation for each cube orientation
colorPerm[ 0] = new Array(0,1,2,3,4,5);
colorPerm[ 1] = new Array(0,2,4,3,5,1);
colorPerm[ 2] = new Array(0,4,5,3,1,2);
colorPerm[ 3] = new Array(0,5,1,3,2,4);
colorPerm[ 4] = new Array(1,0,5,4,3,2);
colorPerm[ 5] = new Array(1,2,0,4,5,3);
colorPerm[ 6] = new Array(1,3,2,4,0,5);
colorPerm[ 7] = new Array(1,5,3,4,2,0);
colorPerm[ 8] = new Array(2,0,1,5,3,4);
colorPerm[ 9] = new Array(2,1,3,5,4,0);
colorPerm[10] = new Array(2,3,4,5,0,1);
colorPerm[11] = new Array(2,4,0,5,1,3);
colorPerm[12] = new Array(3,1,5,0,4,2);
colorPerm[13] = new Array(3,2,1,0,5,4);
colorPerm[14] = new Array(3,4,2,0,1,5);
colorPerm[15] = new Array(3,5,4,0,2,1);
colorPerm[16] = new Array(4,0,2,1,3,5);
colorPerm[17] = new Array(4,2,3,1,5,0);
colorPerm[18] = new Array(4,3,5,1,0,2);
colorPerm[19] = new Array(4,5,0,1,2,3);
colorPerm[20] = new Array(5,0,4,2,3,1);
colorPerm[21] = new Array(5,1,0,2,4,3);
colorPerm[22] = new Array(5,3,1,2,0,4);
colorPerm[23] = new Array(5,4,3,2,1,0);
 
// get all the form settings from the url parameters
function parse() {
	var s="";
	var urlquery=location.href.split("?")
	if(urlquery.length>1){
		var urlterms=urlquery[1].split("&")
		for( var i=0; i<urlterms.length; i++){
			var urllr=urlterms[i].split("=");
			if(urllr[0]=="size") {
				if(urllr[1]-0 >= 2 ) size=urllr[1]-0;
			} else if(urllr[0]=="len") {
				if(urllr[1]-0 >= 1 ) seqlen=urllr[1]-0;
			} else if(urllr[0]=="num"){
				if(urllr[1]-0 >= 1 ) numcub=urllr[1]-0;
			} else if(urllr[0]=="multi") {
				mult=(urllr[1]=="on");
			} else if(urllr[0]=="cubori") {
				cubeorient=(urllr[1]=="on");
			} else if(urllr[0]=="col") {
				if(urllr[1].length==6) colorString = urllr[1];
			}
		}
	}
 
	// expand colour string into 6 actual html color names
	for(var k=0; k<6; k++){
		colors[k]=colorList.length-3;	// gray
		for( var i=0; i<colorList.length; i+=3 ){
			if( colorString.charAt(k)==colorList[i] ){
				colors[k]=i;
				break;
			}
		}
	}
}
 
// append set of moves along an axis to current sequence in order
function appendmoves( sq, axsl, tl, la ){
	for( var sl=0; sl<tl; sl++){	// for each move type
		if( axsl[sl] ){				// if it occurs
			var q=axsl[sl]-1;
 
			// get semi-axis of this move
			var sa = la;
			var m = sl;
			if(sl+sl+1>=tl){ // if on rear half of this axis
				sa+=3; // get semi-axis (i.e. face of the move)
				m=tl-1-m; // slice number counting from that face
				q=2-q; // opposite direction when looking at that face
			}
			// store move
			sq[sq.length]=(m*6+sa)*4+q;
		}
	}
}
 
// generate sequence of scambles
function scramble(){
	//tl=number of allowed moves (twistable layers) on axis -- middle layer ignored
	var tl=size;
	if(mult || (size&1)!=0 ) tl--;
	//set up bookkeeping
	var axsl=new Array(tl);    // movement of each slice/movetype on this axis
	var axam=new Array(0,0,0); // number of slices moved each amount
	var la; // last axis moved
 
	// for each cube scramble
	for( n=0; n<numcub; n++){
		// initialise this scramble
		la=-1;
		seq[n]=new Array(); // moves generated so far
		// reset slice/direction counters
		for( var i=0; i<tl; i++) axsl[i]=0;
		axam[0]=axam[1]=axam[2]=0;
		var moved = 0;
 
		// while generated sequence not long enough
		while( seq[n].length + moved <seqlen ){
 
			var ax, sl, q;
			do{
				do{
					// choose a random axis
					ax=Math.floor(Math.random()*3);
					// choose a random move type on that axis
					sl=Math.floor(Math.random()*tl);
					// choose random amount
					q=Math.floor(Math.random()*3);
				}while( ax==la && axsl[sl]!=0 );		// loop until have found an unused movetype
			}while( ax==la					// loop while move is reducible: reductions only if on same axis as previous moves
					&& !mult				// multislice moves have no reductions so always ok
					&& tl==size				// only even-sized cubes have reductions (odds have middle layer as reference)
					&& (
						2*axam[0]==tl ||	// reduction if already have half the slices move in same direction
						2*axam[1]==tl ||
						2*axam[2]==tl ||
						(
							2*(axam[q]+1)==tl	// reduction if move makes exactly half the slices moved in same direction and
							&&
							axam[0]+axam[1]+axam[2]-axam[q] > 0 // some other slice also moved
						)
				    )
			);
 
			// if now on different axis, dump cached moves from old axis
			if( ax!=la ) {
				appendmoves( seq[n], axsl, tl, la );
				// reset slice/direction counters
				for( var i=0; i<tl; i++) axsl[i]=0;
				axam[0]=axam[1]=axam[2]=0;
				moved = 0;
				// remember new axis
				la=ax;
			}
 
			// adjust counters for this move
			axam[q]++;// adjust direction count
			moved++;
			axsl[sl]=q+1;// mark the slice has moved amount
 
		}
		// dump the last few moves
		appendmoves( seq[n], axsl, tl, la );
 
		// do a random cube orientation if necessary
		seq[n][seq[n].length]= cubeorient ? Math.floor(Math.random()*24) : 0;
	}
 
	// build lookup table
	flat2posit=new Array(12*size*size);
	for(i=0; i<flat2posit.length; i++) flat2posit[i]=-1;
	for(i=0; i<size; i++){
		for(j=0; j<size; j++){
			flat2posit[4*size*(3*size-i-1)+  size+j  ]=        i *size+j;	//D
			flat2posit[4*size*(  size+i  )+  size-j-1]=(  size+i)*size+j;	//L
			flat2posit[4*size*(  size+i  )+4*size-j-1]=(2*size+i)*size+j;	//B
			flat2posit[4*size*(       i  )+  size+j  ]=(3*size+i)*size+j;	//U
			flat2posit[4*size*(  size+i  )+2*size+j  ]=(4*size+i)*size+j;	//R
			flat2posit[4*size*(  size+i  )+  size+j  ]=(5*size+i)*size+j;	//F
		}
	}
 
/*
       19                32
   16           48           35
       31   60      51   44
   28     80    63    67     47
              83  64
          92          79
              95  76
 
                 0
             12     3
                15
*/
}
 
function scramblestring(n){
	var s="",j;
	for(var i=0; i<seq[n].length-1; i++){
		if( i!=0 ) s+=" ";
		var k=seq[n][i]>>2;
 
		j=k%6; k=(k-j)/6;
		if( k && size<=5 && !mult ) {
			s+="dlburf".charAt(j);	// use lower case only for inner slices on 4x4x4 or 5x5x5
		}else{
			if(size<=5 && mult ){
				s+="DLBURF".charAt(j);
				if(k) s+="w";	// use w only for double layers on 4x4x4 and 5x5x5
			}
			else{
				if(k)	s+=(k+1);
				s+="DLBURF".charAt(j);
			}
		}
 
		j=seq[n][i]&3;
		if(j!=0) s+=" 2'".charAt(j);
	}
 
	// add cube orientation
	if( cubeorient ){
		var ori = seq[n][seq[n].length-1];
		s="Top:"+colorList[ 2+colors[colorPerm[ori][3]] ]
			+"&nbsp;&nbsp;&nbsp;Front:"+colorList[2+ colors[colorPerm[ori][5]] ]+"<br>"+s;
	}
	return s;
}
 
function imagestring(nr){
	var s="",i,f,d=0,q;
 
	// initialise colours
	for( i=0; i<6; i++)
		for( f=0; f<size*size; f++)
			posit[d++]=i;
 
	// do move sequence
	for(i=0; i<seq[nr].length-1; i++){
		q=seq[nr][i]&3;
		f=seq[nr][i]>>2;
		d=0;
		while(f>5) { f-=6; d++; }
		do{
			doslice(f,d,q+1);
			d--;
		}while( mult && d>=0 );
	}
 
	// build string containing cube
	var ori = seq[nr][seq[nr].length-1];
	d=0;
	var imageheight = 160; // height of cube images in pixels (160px is a good height for fitting 5 images on a sheet of paper)
	var stickerheight = Math.floor(imageheight/(size*3));
	if(stickerheight < 5) { stickerheight = 5; } // minimum sticker size of 5px, takes effect when cube size reaches 11
	s="<div style='width:"+(stickerheight*size*4)+"px; height:"+(stickerheight*size*3)+"px;'>";
	for(i=0;i<3*size;i++){
		s+="<div style='float: left; display: block; height: "+stickerheight+"px; width: "+(stickerheight*size*4)+"px; line-height: 0px;'>";
		for(f=0;f<4*size;f++){
			if(flat2posit[d]<0){
				s+="<div style='overflow: hidden; display: block; float: left; height: "+stickerheight+"px; width: "+stickerheight+"px;'></div>";
			}else{
				var c = colorPerm[ori][posit[flat2posit[d]]];
				s+="<div style='overflow: hidden; display: block; float: left; border: 1px solid #000; height: "+(stickerheight*1-2)+"px; width: "+(stickerheight*1-2)+"px;'><img src='scrbg/"+colorList[colors[c]+1]+"' /></div>";
			}
			d++;
		}
		s+="</div>";
	}
	s+="</div>";
	return(s);
}
 
function doslice(f,d,q){
	//do move of face f, layer d, q quarter turns
	var f1,f2,f3,f4;
	var s2=size*size;
	var c,i,j,k;
	if(f>5)f-=6;
	// cycle the side facelets
	for(k=0; k<q; k++){
		for(i=0; i<size; i++){
			if(f==0){
				f1=6*s2-size*d-size+i;
				f2=2*s2-size*d-1-i;
				f3=3*s2-size*d-1-i;
				f4=5*s2-size*d-size+i;
			}else if(f==1){
				f1=3*s2+d+size*i;
				f2=3*s2+d-size*(i+1);
				f3=  s2+d-size*(i+1);
				f4=5*s2+d+size*i;
			}else if(f==2){
				f1=3*s2+d*size+i;
				f2=4*s2+size-1-d+size*i;
				f3=	 d*size+size-1-i;
				f4=2*s2-1-d-size*i;
			}else if(f==3){
				f1=4*s2+d*size+size-1-i;
				f2=2*s2+d*size+i;
				f3=  s2+d*size+i;
				f4=5*s2+d*size+size-1-i;
			}else if(f==4){
				f1=6*s2-1-d-size*i;
				f2=size-1-d+size*i;
				f3=2*s2+size-1-d+size*i;
				f4=4*s2-1-d-size*i;
			}else if(f==5){
				f1=4*s2-size-d*size+i;
				f2=2*s2-size+d-size*i;
				f3=s2-1-d*size-i;
				f4=4*s2+d+size*i;
			}
			c=posit[f1];
			posit[f1]=posit[f2];
			posit[f2]=posit[f3];
			posit[f3]=posit[f4];
			posit[f4]=c;
		}
 
		/* turn face */
		if(d==0){
			for(i=0; i+i<size; i++){
				for(j=0; j+j<size-1; j++){
					f1=f*s2+         i+         j*size;
					f3=f*s2+(size-1-i)+(size-1-j)*size;
					if(f<3){
						f2=f*s2+(size-1-j)+         i*size;
						f4=f*s2+         j+(size-1-i)*size;
					}else{
						f4=f*s2+(size-1-j)+         i*size;
						f2=f*s2+         j+(size-1-i)*size;
					}
					c=posit[f1];
					posit[f1]=posit[f2];
					posit[f2]=posit[f3];
					posit[f3]=posit[f4];
					posit[f4]=c;
				}
			}
		}
	}
}
 
function help(){
	alert("Cube Scrambler\n\n"+
		"This cube scrambler can scramble a cube of any size.\n"+
		"Enter the cube size, the number of scrambles you want,\n"+
		"and the length of each scramble (in htm). If you then\n"+
		"press the Scramble button the page will reload and show\n"+
		"the new scrambles. Every time you then reload the page\n"+
		"or click the button, a new set of scrambles is generated.\n"+
 
		"\nFurther options:\n"+
		"Colours: The colour scheme to use in the previews. It\n"+
		"consists of 6 letters, the first letter of the colours\n"+
		"to use on the faces in DLBURF order. Allowed colours are\n"+
		"yellow, blue, red, white, green, orange, purple.\n"+
		"Multi-slice: If clear, an inner slice move is just a\n"+
		"single slice. If checked, an inner slice move means a\n"+
		"turn of the inner slice and all slices lying further\n"+
		"outwards as a single unit.\n"+
		"Cube Orient: If chosen, a random cube orientation is\n"+
		"chosen for each scramble.\n"+
 
		"\nScrambles:\n"+
		"The scrambles will not contain any moves that cancel\n"+
		"each other, nor moves that simplify to a cube rotation.\n"+
 
		"\nNotation:\n"+
		"Standard FLUBRD notation is used for the 2x2x2 and\n"+
		"3x3x3 cubes. With 4x4x4 and 5x5x5 cubes this is extended\n"+
		"with lower case letters flubrd indicating a turn of an\n"+
		"inner slice only, or in multi-slice mode the face letter\n"+
		"is followed by a w to indicate a 'wide' move. For even\n"+
		"larger cubes, inner slices are denoted by \n"+
		"notation.\n"+
		"Tip: On a 2x2x2 cube normally all 6 faces can be turned,\n"+
		"but if Multi-Slice is on, only the RFU faces are used.\n"+
 
		"\nPrinting:\n"+
		"The cube layout might not print correctly on a colour\n"+
		"printer. Make sure that your browser is set up to print\n"+
		"background colours, which is an Internet Options/Advanced\n"+
		"setting in Internet Explorer, or a setting in the Print\n"+
		"dialog in Mozilla Firefox.\n"+
 
		"\nWritten by Jaap Scherphuis, Copyright 2004-2008.");
}
 
parse();
function setForm(){
	document.frm.size.value=size;
	document.frm.len.value=seqlen;
	document.frm.num.value=numcub;
	document.frm.multi.checked=mult;
	document.frm.cubori.checked=cubeorient;
	document.frm.col.value=colorString;
 
	document.frm.subbutton.focus();
}