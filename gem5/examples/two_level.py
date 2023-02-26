def cache_gem5(data):

    s = ""
    s += "from __future__ import print_function\n"
    s += "from __future__ import absolute_import\n"

    s += "import m5\n"
    s += "from m5.objects import *\n"   

    # import the caches which we made
    s += "from cad4u.gem5.examples.caches import *\n"

    # import the SimpleOpts module
    s += "from cad4u.gem5.examples import SimpleOpts\n"

    # Set the usage message to display
    #s += "SimpleOpts.set_usage(\"usage: %prog [options] <binary to execute>\")\n"

    # Finalize the arguments and grab the opts so we can pass it on to our objects
    s += "(opts, args) = SimpleOpts.parse_args()\n"

    # get ISA for the default binary to run. This is mostly for simple testing
    #s += "isa = str(m5.defines.buildEnv['TARGET_ISA']).lower()\n"

    # Default to running 'hello', use the compiled ISA to find the binary
    # grab the specific path to the binary
    s += "binary = os.path.join('%s')\n" %data['binary']

    # create the system we are going to simulate
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

    # Create an L1 instruction and data cache
    s += "system.cpu.icache = L1ICache(size=16,opts=opts)\n"
    s += "system.cpu.dcache = L1DCache(size=%d,opts=opts)\n" %(data['size_l1']) 

    # Connect the instruction and data caches to the CPU
    s += "system.cpu.icache.connectCPU(system.cpu)\n"
    s += "system.cpu.dcache.connectCPU(system.cpu)\n"

    # Create a memory bus, a coherent crossbar, in this case
    s += "system.l2bus = L2XBar()\n"

    # Hook the CPU ports up to the l2bus
    s += "system.cpu.icache.connectBus(system.l2bus)\n"
    s += "system.cpu.dcache.connectBus(system.l2bus)\n"

    # Create an L2 cache and connect it to the l2bus
    s += "system.l2cache = L2Cache(size=%d,opts=opts)\n" %(data['size_l1'])
    s += "system.l2cache.connectCPUSideBus(system.l2bus)\n"

    # Create a memory bus
    s += "system.membus = SystemXBar()\n"

    # Connect the L2 cache to the membus
    s += "system.l2cache.connectMemSideBus(system.membus)\n"

    # create the interrupt controller for the CPU
    s += "system.cpu.createInterruptController()\n"

    # For x86 only, make sure the interrupts are connected to the memory
    # Note: these are directly connected to the memory bus and are not cached
    if data["arch"] == "X86":
        s += "system.cpu.interrupts[0].pio = system.membus.mem_side_ports\n"
        s += "system.cpu.interrupts[0].int_requestor = system.membus.cpu_side_ports\n"
        s += "system.cpu.interrupts[0].int_responder = system.membus.mem_side_ports\n"

    # Connect the system up to the membus
    s += "system.system_port = system.membus.cpu_side_ports\n"

    # Create a DDR3 memory controller
    s += "system.mem_ctrl = MemCtrl()\n"
    s += "system.mem_ctrl.dram = %s_8x8()\n" %(data['memory'])
    s += "system.mem_ctrl.dram.range = system.mem_ranges[0]\n"
    s += "system.mem_ctrl.port = system.membus.mem_side_ports\n"

    # Create a process for a simple "Hello World" application
    s += "process = Process()\n"
    # Set the command
    # cmd is a list which begins with the executable (like argv)
    s += "process.cmd = [binary]\n"

    s += "system.workload = SEWorkload.init_compatible(binary)\n"

    # Set the cpu to use the process as its workload and create thread contexts
    s += "system.cpu.workload = process\n"
    s += "system.cpu.createThreads()\n"

    # set up the root SimObject and start the simulation
    s += "root = Root(full_system = False, system = system)\n"
    # instantiate all of the objects we've created above
    s += "m5.instantiate()\n"

    s += "print('Beginning simulation!')\n"
    s += "exit_event = m5.simulate()\n"
    s += "print('Exiting @ tick %i because %s' % (m5.curTick(), exit_event.getCause()))\n"

    f = open("/content/gem5_code.py","w")
    f.write(s)
    f.close()
