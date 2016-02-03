if [ `whoami` == 'zahmed' ]; then
    ZUNM='mzee1000';
else
    ZUNM=`whoami`;
fi
if [ $UID -eq 0 ]; then
    PS1=$'\[\e[1;31m\]boss\[\e[m\] \[\e[1;34m\][\w]\[\e[m\]\n \[\e[1;31m\]\u306e\[\e[m\]\[\e[32m\] ';
    #PS1='\[\e[0;31m\]boss\[\e[m\] \[\e[1;34m\]\w\[\e[m\] \[\e[0;31m\]<-> \[\e[m\]\[\e[32m\]';
else
    PS1=$'\[\e[1;32m\]hacker-`echo $ZUNM`\[\e[m\] \[\e[1;34m\][\w]\[\e[m\]\n \[\e[1;32m\]\u12a1\[\e[m\] \[\e[37m\]';
    #PS1='\[\e[0;32m\]hacker\[\e[m\] \[\e[1;34m\]\w\[\e[m\] \[\e[1;32m\] -> \[\e[m\] \[\e[37m\]';
fi

