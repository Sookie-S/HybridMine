#!/usr/bin/perl

use strict;
use warnings;
use Cwd qw(cwd);

my $dir = cwd;  

my $newHit = 0;
my $newID = 0;
my $geneq;
my $out_filename = "$ARGV[3]/$ARGV[1]-$ARGV[2].csv";

#print ("$ARGV[1]\n");

   
# print "Current directory: $dir\n";
# print ("Output filemane: $out_filename\n");

my $hit_backup;
my $evalue_backup;

open( my $output, ">", $out_filename) or die "Can't open";
print ($output "Sequence,Best Hit,e-value,Identities,Gaps,Identities_info,Gaps_info\n");

my $i = 0;
my $j = 0;
open( my $input, "<", $ARGV[0]) or die "Can't open"; # file containing blast results
while(<$input>) {

	#if($i eq 15){
		#last;
	#}

	#print ("$_\n\n");
	if ($_ =~ m/Query= (\S+) .+$/ and $newHit == 0) {
	# print ("\n---------------\n");
	#if ($newHit == 0 and $_ =~ m/^Query= (\S+).+ (\S+)$/) {
		$i = $i +1;
		#Look for the "Query=" tag to start looking for the hit line. Get the name of the queried gene.
		$newHit = 1;
		$newID = 1;
		$geneq = $1;
		# print ("$_");
		# print ("\ngeneq : $geneq\n");
		#last; # equivalent of break
		# print ("new hit value : $newHit\n");
	}

	if ( $newHit == 1 and $_ =~ m/No hits found/ or $_ =~ m/> NP_/) {
	#elsif ($newHit == 1 and $_ =~ m/No hits found/ or $_ =~ m/> NP_/) {

		#We have a ***** No hits found ***** result or we skipped the first (self) hit and we stop looking when the first "> id" tag arrives (end of hits table).
		$newHit = 0;
		$j = $j+1;
		# print("\n$_");
		#print("new hit value : $newHit\n");
	}

	my $hit;
	my $evalue = 0;

	#if ( $newHit == 1 and $_ =~ m/^  (\S+\.\d)/ ) {
	if ( $newHit == 1 and ($_ =~ m/^  (\S+\.\d)/ or $_ =~ m/^  (\S+)/)) {
		#We have a new query and we look for the first hit line that comes. Since they are already ordered by e-value.
		#print ("\nline : $_"); #(ex: XP_018224050.1 hypothetical protein DI49_0001, partial [Sacchar...  44.7    1e-05)
		#print("d1 : $1\n");

		if ( $1 ne $geneq) {
			#print ("$1\t $geneq\n");
			#Ignore self-match for paralog search
			$hit = $1;
			$hit_backup = $hit;
			if ( $_ =~ m/\b(\S+)$/ or $_ =~ m/\S+\s+(0.0)\s*$/) {
				$evalue = $1;
				$evalue_backup = $evalue;
				#print ("evalue : $evalue. test : $1\n");
				#print ("$_\n");
			}	

			#print ($output "$ARGV[1].$geneq,$ARGV[2].$hit,$evalue," );
			$newHit = 0;
		}

	}

	my $idLine;
	my $identities;
	my $gaps;

	if ( $newID == 1 and ($_ =~ m/\s*Identities = \d+\/\d+ \(\w+\%\), Gaps = \d+\/\d+ \(\w+\%\)$/)) {
		# print ($_);


		$idLine = $_;
		$identities = $1 if ($_ =~ /Identities = \d+\/\d+ \((\w+)\%\)/);
		$gaps = $1 if ($_ =~ /Gaps = \d+\/\d+ \((\w+)\%\)/);

		# print ("\nLine: $idLine");
		# print ("\nIdentities: $identities");
		# print ("\nGaps: $gaps\n");

		print ($output "$ARGV[1].$geneq,$ARGV[2].$hit_backup,$evalue_backup,$identities,$gaps,$idLine" );

		$newID = 0;
	}
                #print ("IDENTITY FOUND");
		#print ($_);
	
}
close($input);
close($output);

print( "\n\nQueries (i) = $i\n" );
print( "no hits found = $j\n" );

