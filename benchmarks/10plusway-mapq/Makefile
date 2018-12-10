# defaults
protocols = local udc
hals = 10plusway-mapq.hdf5_gzip2 10plusway-mapq.hdf5_uncmp 10plusway-mapq.mmap
resultsDir = results

benches = blockViz hal2maf
benches =  hal2maf

# UDC debugging
udcDebug = no
ifeq (${udcDebug},yes)
   udcVerbose = --udcVerbose
   protocols = udc
   #hals = 10plusway-mapq.mmap
endif

# gprof
gprof = no
ifeq (${gprof},yes)
    hals = 10plusway-mapq.mmap
    #hals = 10plusway-mapq.hdf5_gzip2
    #protocols = udc
    protocols = local
endif

master = no
ifeq (${master},yes)
  binDir = ~/compbio/compartiveGenomics/projs/hal/src/hal-master-w-make/bin
  hals = 10plusway-mapq.hdf5_gzip2 10plusway-mapq.hdf5_uncmp
  resultsDir = results_master
else
  binDir = ~/compbio/compartiveGenomics/projs/hal/src/hal/bin
endif


blockVizTest = ${binDir}/blockVizTest
hal2maf = ${binDir}/hal2maf


.SECONDARY:

dataDir = ../../data
dataUrl =  http://hgwdev.gi.ucsc.edu/~markd/hal/data
timeCmd = /usr/bin/time -p
udcCacheDir = /data/tmp/${USER}
udcCacheFileDir = /data/tmp/${USER}/http/hgwdev.gi.ucsc.edu/Q7E${USER}/hal/data


run: ${benches:%=run_%_bench}
run_%_bench:
	${MAKE} run_hal bench=$*
run_hal: ${hals:%=run_%_hal}
run_%_hal:
	${MAKE} run_protocol bench=${bench} halBaseName=$*
run_protocol: ${protocols:%=run_%_protocol}
run_%_protocol:
	${MAKE} runBench bench=${bench} halBaseName=${halBaseName} protocol=$*


##
# called with:
#   bench=
#   halBaseName=
#   protocol=udc|local
##

ifeq (${protocol},udc)
  halSpec = ${dataUrl}/${halBaseName}.hal
else
  halSpec = ${dataDir}/${halBaseName}.hal
endif

outDir = ${resultsDir}/${bench}/${halBaseName}
resultBase = ${halBaseName}.${protocol}

runBench: ${outDir}/${resultBase}.time

# run blockviz for one pass for same hal
blkVizSpec1 =  Mouse Human chr10 28000000 28999999
blockVizOps = --doSeq ${udcVerbose} --udcCacheDir ${udcCacheDir}
${resultsDir}/blockViz/${halBaseName}/${resultBase}.time:
	@mkdir -p $(dir $@)
ifeq (${protocol},udc)
	rm -rf ${udcCacheFileDir}/${halBaseName}.hal
endif
	rm -f ${outDir}/${resultBase}.gmon.*
	(GMON_OUT_PREFIX=${outDir}/${resultBase}.gmon ${timeCmd} ${blockVizTest} ${blockVizOps} ${halSpec} ${blkVizSpec1}) >& $@.tmp
	mv -f $@.tmp $@
ifeq (${gprof},yes)
	gprof ${blockVizTest} ${outDir}/${resultBase}.gmon.* >${outDir}/${resultBase}.gprof
	gprof --line ${blockVizTest} ${outDir}/${resultBase}.gmon.* >${outDir}/${resultBase}.lgprof
endif


# run hal2maf

hal2mafSpec = --refGenome Human --refSequence chr22 --start 28000000 --length 10000000
blockVizOps = --udcCacheDir ${udcCacheDir}
${resultsDir}/hal2maf/${halBaseName}/${resultBase}.time:
	@mkdir -p $(dir $@)
ifeq (${protocol},udc)
	rm -rf ${udcCacheFileDir}/${halBaseName}.hal
endif
	rm -f ${outDir}/${resultBase}.gmon.*
	(GMON_OUT_PREFIX=${outDir}/${resultBase}.gmon ${timeCmd} ${hal2maf} ${hal2mafOps} ${hal2mafSpec} ${halSpec} /dev/null) >& $@.tmp
	mv -f $@.tmp $@
ifeq (${gprof},yes)
	gprof ${hal2maf} ${outDir}/${resultBase}.gmon.* >${outDir}/${resultBase}.gprof
	gprof --line ${hal2maf} ${outDir}/${resultBase}.gmon.* >${outDir}/${resultBase}.lgprof
endif


clean:
	rm -rf results
