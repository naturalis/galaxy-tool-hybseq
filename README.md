# galaxy-tool-hybseq
## Galaxy server
This galaxy workflow was created and tested in a local galaxy server. The server was setup by following the tutorial: Galaxy Installation with Ansible (Galaxy Training Materials). https://training.galaxyproject.org/training-material/topics/admin/tutorials/ansible-galaxy/tutorial.html (Rasche et al, 2021)

To run the server, open the galaxy server directory by using the command:
```bash
$ cd /srv/galaxy/server
```
When in this directory run the server by running the run.sh file using the command:
```bash
$ bash run.sh
```
When the server is active it can be accessed at http://localhost:8080/
It is possible port 8080 is already in use, when this is the case kill the process using the command 
```bash
$ sudo kill -9 $(sudo lsof -t -i :8080)
```
## Workflow
In this project we recreated the hybrid sequencing pipeline first described by Nikolov et al. in 2019 in galaxy multiple different pre existing tools as well as custom tools were used in this pipeline. The list below shows all the pre-existing tools and the versions we used.
  - Trimmomatics        0.38.1
  - Fastx_collapser     1.0.1
  - YASRA               2.33
  - Lastz               1.3.2

The workflow also has custom made tools:
  - YASRA step 1: uses LASTZ to map reads to the reference sequence
  - YASRA step 2: finds best hits
  - YASRA step 3: sorts the best hits
  - YASRA step 4: assembly of the hits
  - Extract contigs: creates individual contig sam files for each contig
  - create yaml: creates YAML file which is needed in further steps of the pipeline. 
 
## Tools
The tools we created for the pipeline are available in the /src directory. Before the YASRA tools can be used YASRA needs to be installed on the machine and added to the $PATH. We chose to use YASRA instead of Alignreads because we were not able to get the requirements in the XML-files to work. When running Alignreads in Galaxy we kept getting an error which stated that it was unable to create the Conda environment needed. We were not able to find the reason for this. 

## Galaxy server download
The appliance for the Galaxy server we used in this project is available for download at https://zenodo.org/record/5524661, which can be imported onto a virtualization product like Virtualbox. 
The user we used is called 'natgal' with the password 'naturalis'
  
