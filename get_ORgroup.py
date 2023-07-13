#!/usr/bin/python -w
import sys
import ast


'''
############################################################
##                                                        ##
##       get_ORgroup.py for Windows/Linux                 ##
##              Produced by Johnny S. Ferreira            ##
##                         Last Modified on 05/07/2022    ##
##                                                        ##
############################################################
'''


if len(sys.argv) < 2:
  error = """
    This script compares the SPECIES_NAME.250.fa with the SPECIES_NAME.besthit and saves different
    outputs according to its OR Group presented as the best hit query.

    The following files are necessary at DIRECTORY:
    species.250.fa, species.besthit, OR_groups.txt

    This program generates the following files in the current directory:
    species.alpha.idlist, species.beta.idlist, species.gamma.idlist, species.delta.idlist,
    species.epsilon.idlist, species.zeta.idlist, species.eta.idlist, species.theta1.idlist,
    species.theta2.idlist, species.kappa.idlist, species.lambdaa.idlist, species.amphioxus.idlist

    So, make sure to specify the name of the file. Example:
    python test_ORgroup.py GCA_000004195.4_UCB_Xtro_10.0_genomic2_Theta


    After getting the .idlist, use this to get the corresponding sequences from .250.fa:
    grepfasta.pl GCA_017654675.1_Xenopus_laevis_v10.1_genomic4.alpha.idlist GCA_017654675.1_Xenopus_laevis_v10.1_genomic4.250.fa > GCA_017654675.1_Xenopus_laevis_v10.1_genomic4.alpha.250.fa ;

    and so on...
  """

  print(error)
  sys.exit()


def finding_OR_groups(file):
    name = file
    fasta = open('{}.250.fa'.format(name), 'r') # opens the .250.fa fastafile

    #opening the dictionary with the OR Groups:
    with open('OR_groups.txt') as f:
      data = f.read()

    ORGroups = ast.literal_eval(data) # reconstruct the dictionary using ast

    # OR Group outputs
    pema = open("{}.pema.idlist".format(name), "w+")
    alpha = open("{}.alpha.idlist".format(name), "w+")
    beta = open("{}.beta.idlist".format(name), "w+")
    gamma = open("{}.gamma.idlist".format(name), "w+")
    delta = open("{}.delta.idlist".format(name), "w+")
    epsilon = open("{}.epsilon.idlist".format(name), "w+")
    zeta = open("{}.zeta.idlist".format(name), "w+")
    eta = open("{}.eta.idlist".format(name), "w+")
    theta1 = open("{}.theta1.idlist".format(name), "w+")
    theta2 = open("{}.theta2.idlist".format(name), "w+")
    kappa = open("{}.kappa.idlist".format(name), "w+")
    lambdaa = open("{}.lambdaa.idlist".format(name), "w+")
    amphioxus = open("{}.amphioxus.idlist".format(name), "w+")

    # 1 - reads fasta file
    for line in fasta:
        line = line.rstrip()

        if '>' in line:

          x = line.split('_') # first split by _ getting the init
          y = x[-1].split() # second split to get the end, because it is together with length of the sequence and an 'aa' string

          contig_fasta = x[-3] # the contig name of the fasta file

          init = int(x[-2]) # the penultimate element is the initial one
          end = int(y[0][0:-1]) # get only the end without the direction

          # 2 - reads besthit file
          besthit = open('{}.besthit'.format(name), 'r')
          for lines in besthit:
            lin = lines.split('\n')

            contig = lin[0].split()[3] # the contig name of the best hit
            l = lin[0].split()
            init_besthit = int(l[4])
            end_besthit = int(l[6])

            if ((contig_fasta == contig) and abs(init - init_besthit) < 350 and abs(end - end_besthit) < 350):
              #print(str(init) + ' and ' + str(init_besthit))

              # saves each header in its respective OR group
              for k, v in ORGroups.items(): # k - key; v - value
                if l[0] in ORGroups[k]:
                  if k == 'pema':
                    pema.write(line[1:] + '\n')
                  if k == 'alpha':
                    alpha.write(line[1:] + '\n') # removes the '>' for grepfasta.pl usage
                  elif k == 'beta':
                    beta.write(line[1:] + '\n')
                  elif k == 'gamma':
                    gamma.write(line[1:] + '\n')
                  elif k == 'delta':
                    delta.write(line[1:] + '\n')
                  elif k == 'epsilon':
                    epsilon.write(line[1:] + '\n')
                  elif k == 'zeta':
                    zeta.write(line[1:] + '\n')
                  elif k == 'eta':
                    eta.write(line[1:] + '\n')
                  elif k == 'theta1':
                    theta1.write(line[1:] + '\n')
                  elif k == 'theta2':
                    theta2.write(line[1:] + '\n')
                  elif k == 'kappa':
                    kappa.write(line[1:] + '\n')
                  elif k == 'lambdaa':
                    lambdaa.write(line[1:] + '\n')
                  else:
                    amphioxus.write(line[1:] + '\n')
                  #nam = '_'.join(x[0:8]) # join the name until the contig name
                  #old_name = nam + '_' + x[-2] + '_' + x[-1]
                  #new_name = nam + '_' + k + '_' + x[-2] + '_' + x[-1] # gives a new name for the sequence title including its OR group
                  break


file = str(sys.argv[1])
finding_OR_groups(file)


'''
APÓS do_getseq.pl e get_ORgroup.py

grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.alpha.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.alpha.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.beta.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.beta.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.gamma.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.gamma.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.delta.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.delta.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.epsilon.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.epsilon.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.zeta.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.zeta.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.eta.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.eta.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.theta1.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.theta1.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.theta2.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.theta2.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.kappa.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.kappa.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.lambdaa.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.lambdaa.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.pema.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.pema.250.fa ;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.amphioxus.idlist GCA_009667805.1_ASM966780v1_genomic.250.fa > GCA_009667805.1_ASM966780v1_genomic.amphioxus.250.fa ;
'''



'''
PARA CONVERTER O .del.fa em .fa para o do_funcOR.pl:

grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.alpha.align.del.notdeleted GCA_009667805.1_ASM966780v1_genomic.alpha.align.del.fa > GCA_009667805.1_ASM966780v1_genomic.alpha.fa;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.beta.align.del.notdeleted GCA_009667805.1_ASM966780v1_genomic.beta.align.del.fa > GCA_009667805.1_ASM966780v1_genomic.beta.fa;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.gamma.align.del.notdeleted GCA_009667805.1_ASM966780v1_genomic.gamma.align.del.fa > GCA_009667805.1_ASM966780v1_genomic.gamma.fa;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.delta.align.del.notdeleted GCA_009667805.1_ASM966780v1_genomic.delta.align.del.fa > GCA_009667805.1_ASM966780v1_genomic.delta.fa;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.epsilon.align.del.notdeleted GCA_009667805.1_ASM966780v1_genomic.epsilon.align.del.fa > GCA_009667805.1_ASM966780v1_genomic.epsilon.fa;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.eta.align.del.notdeleted GCA_009667805.1_ASM966780v1_genomic.eta.align.del.fa > GCA_009667805.1_ASM966780v1_genomic.eta.fa;
grepfasta.pl GCA_009667805.1_ASM966780v1_genomic.zeta.align.del.notdeleted GCA_009667805.1_ASM966780v1_genomic.zeta.align.del.fa > GCA_009667805.1_ASM966780v1_genomic.zeta.fa;

'''


'''
PARA DELTA, EPSION E ETA ENQUANTO O DO_FUNCOR É REALIZADO:

cat GCA_009667805.1_ASM966780v1_genomic.delta.fa for_amphioxus_analysis_through_phylogenetics_tree.fas Outgroups_aa.fas > GCA_009667805.1_ASM966780v1_genomic.delta2.fa ;

cat GCA_009667805.1_ASM966780v1_genomic.epsilon.fa for_amphioxus_analysis_through_phylogenetics_tree.fas Outgroups_aa.fas > GCA_009667805.1_ASM966780v1_genomic.epsilon2.fa ;

cat GCA_009667805.1_ASM966780v1_genomic.eta.fa for_amphioxus_analysis_through_phylogenetics_tree.fas Outgroups_aa.fas > GCA_009667805.1_ASM966780v1_genomic.eta2.fa ;

cat GCA_009667805.1_ASM966780v1_genomic.zeta.fa for_amphioxus_analysis_through_phylogenetics_tree.fas Outgroups_aa.fas > GCA_009667805.1_ASM966780v1_genomic.zeta2.fa ;

mafft --auto GCA_009667805.1_ASM966780v1_genomic.delta2.fa > GCA_009667805.1_ASM966780v1_genomic.delta3.fa ;

mafft --auto GCA_009667805.1_ASM966780v1_genomic.epsilon2.fa > GCA_009667805.1_ASM966780v1_genomic.epsilon3.fa ;

mafft --auto GCA_009667805.1_ASM966780v1_genomic.eta2.fa > GCA_009667805.1_ASM966780v1_genomic.eta3.fa ;

mafft --auto GCA_009667805.1_ASM966780v1_genomic.zeta2.fa > GCA_009667805.1_ASM966780v1_genomic.zeta3.fa ;




ETAPA DO_FUNCOR.PL PARA REMOVER AS QUERIES COM O .notdeleted


grepfasta.pl GCA_905171765.1_aBufBuf1.1_genomic2.alpha.align.del.notdeleted GCA_905171765.1_aBufBuf1.1_genomic2.alpha.align.del.fa > GCA_905171765.1_aBufBuf1.1_genomic2.alpha.fa ;
grepfasta.pl GCA_905171765.1_aBufBuf1.1_genomic2.beta.align.del.notdeleted GCA_905171765.1_aBufBuf1.1_genomic2.beta.align.del.fa > GCA_905171765.1_aBufBuf1.1_genomic2.beta.fa ;
grepfasta.pl GCA_905171765.1_aBufBuf1.1_genomic2.gamma.align.del.notdeleted GCA_905171765.1_aBufBuf1.1_genomic2.gamma.align.del.fa > GCA_905171765.1_aBufBuf1.1_genomic2.gamma.fa
grepfasta.pl GCA_905171765.1_aBufBuf1.1_genomic2.delta.align.del.notdeleted GCA_905171765.1_aBufBuf1.1_genomic2.delta.align.del.fa > GCA_905171765.1_aBufBuf1.1_genomic2.delta.fa ;
grepfasta.pl GCA_905171765.1_aBufBuf1.1_genomic2.epsilon.align.del.notdeleted GCA_905171765.1_aBufBuf1.1_genomic2.epsilon.align.del.fa > GCA_905171765.1_aBufBuf1.1_genomic2.epsilon.fa ;
grepfasta.pl GCA_905171765.1_aBufBuf1.1_genomic2.eta.align.del.notdeleted GCA_905171765.1_aBufBuf1.1_genomic2.eta.align.del.fa > GCA_905171765.1_aBufBuf1.1_genomic2.eta.fa ;
grepfasta.pl GCA_905171765.1_aBufBuf1.1_genomic2.zeta.align.del.notdeleted GCA_905171765.1_aBufBuf1.1_genomic2.zeta.align.del.fa > GCA_905171765.1_aBufBuf1.1_genomic2.zeta.fa ;


PARA DELTA, EPSILON, ETA E ZETA
cat GCA_905171765.1_aBufBuf1.1_genomic2.delta.fa for_amphioxus_analysis_through_phylogenetics_tree.fas Outgroups_aa.fas > GCA_905171765.1_aBufBuf1.1_genomic2.delta2.fa ;
cat GCA_905171765.1_aBufBuf1.1_genomic2.epsilon.fa for_amphioxus_analysis_through_phylogenetics_tree.fas Outgroups_aa.fas > GCA_905171765.1_aBufBuf1.1_genomic2.epsilon2.fa ;
cat GCA_905171765.1_aBufBuf1.1_genomic2.eta.fa for_amphioxus_analysis_through_phylogenetics_tree.fas Outgroups_aa.fas > GCA_905171765.1_aBufBuf1.1_genomic2.eta2.fa ;
cat GCA_905171765.1_aBufBuf1.1_genomic2.zeta.fa for_amphioxus_analysis_through_phylogenetics_tree.fas Outgroups_aa.fas > GCA_905171765.1_aBufBuf1.1_genomic2.zeta2.fa ;

mafft --auto GCA_905171765.1_aBufBuf1.1_genomic2.delta2.fa > GCA_905171765.1_aBufBuf1.1_genomic2.delta3.fa ;
mafft --auto GCA_905171765.1_aBufBuf1.1_genomic2.epsilon2.fa > GCA_905171765.1_aBufBuf1.1_genomic2.epsilon3.fa ;
mafft --auto GCA_905171765.1_aBufBuf1.1_genomic2.eta2.fa > GCA_905171765.1_aBufBuf1.1_genomic2.eta3.fa ;
mafft --auto GCA_905171765.1_aBufBuf1.1_genomic2.zeta2.fa > GCA_905171765.1_aBufBuf1.1_genomic2.zeta3.fa ;


ANTES DE JOGAR NO GENEIOUS, É PRECISO O MAFFT DE .func.fa e do .align.del.fa

mafft --auto GCA_019650415.1_UCB_Ppar_1.0_genomic.alpha.func.fa > GCA_019650415.1_UCB_Ppar_1.0_genomic.alpha.func2.fa ;
mafft --auto GCA_019650415.1_UCB_Ppar_1.0_genomic.beta.func.fa > GCA_019650415.1_UCB_Ppar_1.0_genomic.beta.func2.fa ;
mafft --auto GCA_019650415.1_UCB_Ppar_1.0_genomic.gamma.func.fa > GCA_019650415.1_UCB_Ppar_1.0_genomic.gamma.func2.fa ;
mafft --auto GCA_019650415.1_UCB_Ppar_1.0_genomic.delta.align.del.fa > GCA_019650415.1_UCB_Ppar_1.0_genomic.delta.align.del2.fa ;
mafft --auto GCA_019650415.1_UCB_Ppar_1.0_genomic.epsilon.align.del.fa > GCA_019650415.1_UCB_Ppar_1.0_genomic.epsilon.align.del2.fa ;
mafft --auto GCA_019650415.1_UCB_Ppar_1.0_genomic.eta.align.del.fa > GCA_019650415.1_UCB_Ppar_1.0_genomic.eta.align.del2.fa ;



PARA DESALINHAR OS FUNC2
awk '{ if ($0 !~ /^>/) { gsub("-", "",$0); } print $0; }' GCA_009364415.1_usc_Smult_1.0_genomic.alpha.func2.fasta > GCA_009364415.1_usc_Smult_1.0_genomic.alpha.unligned.func2.fasta ;
awk '{ if ($0 !~ /^>/) { gsub("-", "",$0); } print $0; }' GCA_009364415.1_usc_Smult_1.0_genomic.beta.func2.fasta > GCA_009364415.1_usc_Smult_1.0_genomic.beta.unligned.func2.fasta ;
awk '{ if ($0 !~ /^>/) { gsub("-", "",$0); } print $0; }' GCA_009364415.1_usc_Smult_1.0_genomic.gamma.func2.fasta > GCA_009364415.1_usc_Smult_1.0_genomic.gamma.unligned.func2.fasta ;
awk '{ if ($0 !~ /^>/) { gsub("-", "",$0); } print $0; }' GCA_009364415.1_usc_Smult_1.0_genomic.delta.func2.fasta > GCA_009364415.1_usc_Smult_1.0_genomic.delta.unligned.func2.fasta ;
awk '{ if ($0 !~ /^>/) { gsub("-", "",$0); } print $0; }' GCA_009364415.1_usc_Smult_1.0_genomic.epsilon.func2.fasta > GCA_009364415.1_usc_Smult_1.0_genomic.epsilon.unligned.func2.fasta ;
awk '{ if ($0 !~ /^>/) { gsub("-", "",$0); } print $0; }' GCA_009364415.1_usc_Smult_1.0_genomic.eta.func2.fasta > GCA_009364415.1_usc_Smult_1.0_genomic.eta.unligned.func2.fasta ;





DEPOIS DA SEPARAÇÃO DOS GRUPOS DO genome.pseudogenes.fa;
grepfasta.pl GCA_009364415.1_usc_Smult_1.0_genomic.alpha.idlist GCA_009364415.1_usc_Smult_1.0_genomic.pseudogenes.fa > GCA_009364415.1_usc_Smult_1.0_genomic.alpha.pseudogenes.fa;
grepfasta.pl GCA_009364415.1_usc_Smult_1.0_genomic.beta.idlist GCA_009364415.1_usc_Smult_1.0_genomic.pseudogenes.fa > GCA_009364415.1_usc_Smult_1.0_genomic.beta.pseudogenes.fa;
grepfasta.pl GCA_009364415.1_usc_Smult_1.0_genomic.delta.idlist GCA_009364415.1_usc_Smult_1.0_genomic.pseudogenes.fa > GCA_009364415.1_usc_Smult_1.0_genomic.delta.pseudogenes.fa;
grepfasta.pl GCA_009364415.1_usc_Smult_1.0_genomic.eta.idlist GCA_009364415.1_usc_Smult_1.0_genomic.pseudogenes.fa > GCA_009364415.1_usc_Smult_1.0_genomic.eta.pseudogenes.fa;
grepfasta.pl GCA_009364415.1_usc_Smult_1.0_genomic.gamma.idlist GCA_009364415.1_usc_Smult_1.0_genomic.pseudogenes.fa > GCA_009364415.1_usc_Smult_1.0_genomic.gamma.pseudogenes.fa;
grepfasta.pl GCA_009364415.1_usc_Smult_1.0_genomic.epsilon.idlist GCA_009364415.1_usc_Smult_1.0_genomic.pseudogenes.fa > GCA_009364415.1_usc_Smult_1.0_genomic.epsilon.pseudogenes.fa;

'''
