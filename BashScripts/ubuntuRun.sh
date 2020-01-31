runningVmu=$(VBoxManage list runningvms)
s=$runningVmu
a=( $s )
runningVm=${a[0]}
echo $runningVm
#runningVm=($runningVmu)   #to remove uuid and only get name
temp="${runningVm%\"}"    # next few lines to convert "VMName" to VMName
temp="${temp#\"}"
echo "$temp"
runningVm=$temp



uuid=$(VBoxManage snapshot $runningVm take snap1)               #keeping the snapshot uuid 
s=$uuid                                                         
a=( $s )
uuid=${a[3]}
echo $uuid

VBoxManage controlvm $runningVm poweroff
VBoxManage snapshot $runningVm restore $uuid
VBoxManage startvm $runningVm
