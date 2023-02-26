def simple_gem5(data):

	s = ""
	s += "from __future__ import print_function\n"
	s += "from __future__ import absolute_import\n"

	s += "import m5\n"
	s += "from m5.objects import *\n"

	s += "system = System()\n"

	# Set the clock fequency of the system (and all of its children)
	s += "system.clk_domain = SrcClockDomain()\n"
	s += "system.clk_domain.clock = '%.1fGHz'\n" %(data['clk'])
	s += "system.clk_domain.voltage_domain = VoltageDomain()\n"

	arch = "X86"
	if data["arch"] == "RISCV":
		arch = "Riscv"
	elif data["arch"] == "ARM":
		arch = "Arm"

	# Create a simple CPU
	if data['cpu'] == 'Simple':
		s += "system.cpu = %sTimingSimpleCPU()\n" %(arch)
		s += "system.mem_mode = 'timing'\n" 
	elif data['cpu'] == 'Out Order':
		s += "system.cpu = %sDerivO3CPU()\n" %(arch)
		s += "system.mem_mode = 'timing'\n"
		s += "system.cpu.createThreads()\n"
	elif data['cpu'] == 'In Order':
		s += "system.cpu = %sAtomicSimpleCPU()\n" %(arch)
		s += "system.mem_mode = 'atomic'\n"
		s += "system.cpu.createThreads()\n" 
	
	s += "system.mem_ranges = [AddrRange('512MB')]\n"

	# Create a memory bus, a system crossbar, in this case
	s += "system.membus = SystemXBar()\n"

	# Hook the CPU ports up to the membus
	s += "system.cpu.icache_port = system.membus.cpu_side_ports\n"
	s += "system.cpu.dcache_port = system.membus.cpu_side_ports\n"

	# create the interrupt controller for the CPU and connect to the membus
	s += "system.cpu.createInterruptController()\n"

	# For x86 only, make sure the interrupts are connected to the memory
	# Note: these are directly connected to the memory bus and are not cached
	if data["arch"] == "X86":
		s += "system.cpu.interrupts[0].pio = system.membus.mem_side_ports\n"
		s += "system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports\n"
		s += "system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports\n"

	# Create a DDR3 memory controller and connect it to the membus
	s += "system.mem_ctrl = MemCtrl()\n"
	s += "system.mem_ctrl.dram = %s_8x8()\n" %(data['memory'])
	s += "system.mem_ctrl.dram.range = system.mem_ranges[0]\n"
	s += "system.mem_ctrl.port = system.membus.mem_side_ports\n"

	# Connect the system up to the membus
	s += "system.system_port = system.membus.cpu_side_ports\n"

	# get ISA for the binary to run.
	#s += "isa = str(m5.defines.buildEnv['TARGET_ISA']).lower()\n"

	# Default to running 'hello', use the compiled ISA to find the binary
	# grab the specific path to the binary
	s += "binary = os.path.join('%s')\n" %data['binary']

	s += "system.workload = SEWorkload.init_compatible(binary)\n"

	# Create a process for a simple "Hello World" application
	s += "process = Process()\n"
	# Set the command
	# cmd is a list which begins with the executable (like argv)
	s += "process.cmd = [binary]\n"
	# Set the cpu to use the process as its workload and create thread contexts
	s += "system.cpu.workload = process\n"
	s += "system.cpu.createThreads()\n"

	# set up the root SimObject and start the simulation
	s += "root = Root(full_system = False, system=system)\n"
	# instantiate all of the objects we've created above
	s += "m5.instantiate()\n"

	s += "print('Beginning simulation!')\n"
	s += "exit_event = m5.simulate()\n"
	s += "print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))\n"

	f = open("/content/gem5_code.py","w")
	f.write(s)
	f.close()
