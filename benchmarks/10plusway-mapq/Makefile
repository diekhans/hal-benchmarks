.SECONDARY:

binDir = ../../bin
dataDir = ../../data
dataUrl =  http://hgwdev.gi.ucsc.edu/~markd/hal/data
timeCmd = /usr/bin/time -p
udcCacheDir = /data/tmp/${USER}
udcCacheFileDir = /data/tmp/${USER}/http/hgwdev.gi.ucsc.edu/Q7E${USER}/hal/data

hals = 10plusway-mapq.hdf5_gzip2 10plusway-mapq.hdf5_uncmp 10plusway-mapq.mmap
protocols = local udc

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

outDir = results/${halBaseName}
resultBase = ${halBaseName}.${protocol}
blkVizSpec1 =  Mouse Human chr22 28000000 28999999
blkVizSpec2 =  Dog Human chr22 38000000 38999999

blockVizBenchFile: ${outDir}/${resultBase}.1.time ${outDir}/${resultBase}.2.time

# run sequentially for same hal
${outDir}/${resultBase}.1.time:
	@mkdir -p $(dir $@)
ifeq (${protocol},udc)
	rm -rf ${udcCacheFileDir}/${halBaseName}.hal
endif
	(${timeCmd} ${binDir}/blockVizTest --doSeq --udcCacheDir ${udcCacheDir} ${halSpec} ${blkVizSpec1}) >& $@.tmp
	mv -f $@.tmp $@

${outDir}/${resultBase}.2.time: ${outDir}/${resultBase}.1.time
	@mkdir -p $(dir $@)
	(${timeCmd} ${binDir}/blockVizTest --doSeq --udcCacheDir ${udcCacheDir} ${halSpec} ${blkVizSpec2}) >& $@.tmp
	mv -f $@.tmp $@
