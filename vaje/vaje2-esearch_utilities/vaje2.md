# Conda commands

```bash
conda list
conda env list
conda info --env
conda install --channel <channel-name> <package-name>
```

# Entrez-Direct commands

```bash
efetch -db <database name> -format [xml|fasta|gb(genebank)] -id <accession number>
efetch -db nuccore -format fasta -id AF086833 -seq_start 1 -seq_stop 3
efetch -db nuccore -format fasta -id AF086833 -seq_start 1 -seq_stop 3 -strand [1|2] # reverse sequence
esearch -db nucleotide -query PRJNA257197 # ta query je ID nekega projekta

esearch -db pubmed -query "Garber ED [AUTH] AND PNAS[JOUR]" | \
> efilter -query "mouse" | \
> efetch -format abstract # efilter --help

esearch -db gene -query "3043[UID]" | \
> elink -target protein -name gene_protein_refseq | \
> efetch -format fasta # einfo -db gene -links

esearch -db gene -query "3043[UID]" | \
> elink -target nuccore -name gene_nuccore_refseqrna | \
> efetch -format gbc | \
> xtract -pattern INSDSeq -element INSDSeq_locus INSDSeq_length
```

epost se uporabi ko imamo podatke v datoteki in želimo iz njih delat poizvedbe

```
$ cat > genids.txt
3039
3040
3042

$ cat genids.txt | \
> epost -db gene -format uid | \
> elink -target nuccore -name gene_nuccore_refseqrna | \
> efetch -format gbc | \
> xtract -pattern INSDSeq -element INSDSeq_locus INSDSeq_length
```

## xtract

xtract ti ekstrahira tags iz xml datoteke. Snip:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE DocumentSummarySet>
<DocumentSummarySet status="OK">
  <DocumentSummary>
    <Id>2238893766</Id>
    <Caption>LC707984</Caption>
    <Title>Ursus thibetanus mitochondrial DNA, D-loop region, partial sequence, isolate: 60</Title>
    <Extra>gi|2238893766|dbj|LC707984.1|</Extra>
    <Gi>2238893766</Gi>
    <CreateDate>2022/05/14</CreateDate>
    <UpdateDate>2022/05/14</UpdateDate>
    <Flags>0</Flags>
    <TaxId>9642</TaxId>
    <Slen>712</Slen>
    <Biomol>genomic</Biomol>
    <MolType>dna</MolType>
    <Topology>linear</Topology>
    <SourceDb>insd</SourceDb>
    <SegSetSize>0</SegSetSize>
    <ProjectId>0</ProjectId>
    <SubType>isolate|tissue_type|dev_stage|country|collection_date</SubType>
    <SubName>60|muscle|adult|Japan:Fukushima|2019-12-11</SubName>
    <AssemblyGi>0</AssemblyGi>
    <GeneticCode>1</GeneticCode>
    <Organism>Ursus thibetanus</Organism>
    <Statistics>
      <Stat type="Length" count="712"/>
      <Stat type="Length" subtype="literal" count="712"/>
      <Stat type="all" count="2"/>
      <Stat type="blob_size" count="1622"/>
      <Stat type="imp" count="1"/>
      <Stat type="imp" subtype="D-loop" count="1"/>
      <Stat type="org" count="1"/>
      <Stat type="pub" count="2"/>
      <Stat type="pub" subtype="unpublished" count="1"/>
      <Stat source="all" type="Length" count="712"/>
      <Stat source="all" type="all" count="2"/>
      <Stat source="all" type="blob_size" count="1622"/>
      <Stat source="all" type="imp" count="1"/>
      <Stat source="all" type="org" count="1"/>
      <Stat source="all" type="pub" count="2"/>
    </Statistics>
    <Properties na="1">1</Properties>
    <OSLT indexed="yes">LC707984.1</OSLT>
    <AccessionVersion>LC707984.1</AccessionVersion>
  </DocumentSummary>
</DocumentSummarySet>
```

Tag je oblike `<ime>`. Najprej uporabiš `-pattern <tag>` in nato še `-element <sub-tag>` (note: nevem
zakaj ne dela za Statistics).

Primer:

```bash
efetch -db nucleotide -id LC707984.1 -format docsum |\
> xtract -pattern DocumentSummary -element Organism,Title,MolType
```
