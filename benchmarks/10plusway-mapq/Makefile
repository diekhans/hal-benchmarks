# defaults
protocols = local udc
hals = 10plusway-mapq.hdf5_gzip2 10plusway-mapq.hdf5_uncmp 10plusway-mapq.mmap
resultsDir = results

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


.SECONDARY:

dataDir = ../../data
dataUrl =  http://hgwdev.gi.ucsc.edu/~markd/hal/data
timeCmd = /usr/bin/time -p
udcCacheDir = /data/tmp/${USER}
udcCacheFileDir = /data/tmp/${USER}/http/hgwdev.gi.ucsc.edu/Q7E${USER}/hal/data


run: ${hals:%=run_%_hal}
run_%_hal:
	${MAKE} run_hal halBaseName=$*
run_hal: ${protocols:%=run_%_hal_protocol}
run_%_hal_protocol:
	${MAKE} run_hal_protocl halBaseName=${halBaseName} protocol=$*
run_hal_protocl: blockVizBenchFile

##
# called with:
#   halBaseName=
#   protocol=udc|local
##

ifeq (${protocol},udc)
  halSpec = ${dataUrl}/${halBaseName}.hal
else
  halSpec = ${dataDir}/${halBaseName}.hal
endif

outDir = ${resultsDir}/${halBaseName}
resultBase = ${halBaseName}.${protocol}
blkVizSpec1 =  Mouse Human chr10 28000000 28999999

blockVizOps = --doSeq ${udcVerbose} --udcCacheDir ${udcCacheDir}

blockVizBenchFile: ${outDir}/${resultBase}.time

# run sequentially for same hal
${outDir}/${resultBase}.time:
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


clean:
	rm -rf results
