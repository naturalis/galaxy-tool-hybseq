# galaxy-tool-hybseq
## Galaxy server
This galaxy workflow was created and tested ion a local galaxy server. The server was setup by following the tutorial: Galaxy Installation with Ansible (Galaxy Training Materials). https://training.galaxyproject.org/training-material/topics/admin/tutorials/ansible-galaxy/tutorial.html (Rasche et al, 2021)

## Workflow
In this project we recreated the hybrid sequencing pipeline first described by Nikolov et al. in 2019 in galaxy multiple different pre existing tools as well as custom tools were used in this pipeline. The list below shows all the pre-existing tools and the versions we used.
  - Trimmomatics        0.38.1
  - Fastx_collapser     1.0.1
  - YASRA               2.33
  - Lastz               1.3.2
  - SAMtools:
    - sam_to_bam       2.1.1
    - sam_pileup       1.1.3
  - VarScan             2.4.2
  - BLAT                0.3
  - MAFFT               7.475
  - MACSE
  - Phyutility          2.7.1
  - Partitionfinder     2.1.1
  - Phylogeny_converter 1.0.0
  - RAxML               8.2.4
  
    
