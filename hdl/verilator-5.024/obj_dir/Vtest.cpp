// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Model implementation (design independent parts)

#include "Vtest__pch.h"

//============================================================
// Constructors

Vtest::Vtest(VerilatedContext* _vcontextp__, const char* _vcname__)
    : VerilatedModel{*_vcontextp__}
    , vlSymsp{new Vtest__Syms(contextp(), _vcname__, this)}
    , data{vlSymsp->TOP.data}
    , en{vlSymsp->TOP.en}
    , reset{vlSymsp->TOP.reset}
    , q{vlSymsp->TOP.q}
    , rootp{&(vlSymsp->TOP)}
{
    // Register model with the context
    contextp()->addModel(this);
}

Vtest::Vtest(const char* _vcname__)
    : Vtest(Verilated::threadContextp(), _vcname__)
{
}

//============================================================
// Destructor

Vtest::~Vtest() {
    delete vlSymsp;
}

//============================================================
// Evaluation function

#ifdef VL_DEBUG
void Vtest___024root___eval_debug_assertions(Vtest___024root* vlSelf);
#endif  // VL_DEBUG
void Vtest___024root___eval_static(Vtest___024root* vlSelf);
void Vtest___024root___eval_initial(Vtest___024root* vlSelf);
void Vtest___024root___eval_settle(Vtest___024root* vlSelf);
void Vtest___024root___eval(Vtest___024root* vlSelf);

void Vtest::eval_step() {
    VL_DEBUG_IF(VL_DBG_MSGF("+++++TOP Evaluate Vtest::eval_step\n"); );
#ifdef VL_DEBUG
    // Debug assertions
    Vtest___024root___eval_debug_assertions(&(vlSymsp->TOP));
#endif  // VL_DEBUG
    vlSymsp->__Vm_deleter.deleteAll();
    if (VL_UNLIKELY(!vlSymsp->__Vm_didInit)) {
        vlSymsp->__Vm_didInit = true;
        VL_DEBUG_IF(VL_DBG_MSGF("+ Initial\n"););
        Vtest___024root___eval_static(&(vlSymsp->TOP));
        Vtest___024root___eval_initial(&(vlSymsp->TOP));
        Vtest___024root___eval_settle(&(vlSymsp->TOP));
    }
    VL_DEBUG_IF(VL_DBG_MSGF("+ Eval\n"););
    Vtest___024root___eval(&(vlSymsp->TOP));
    // Evaluate cleanup
    Verilated::endOfEval(vlSymsp->__Vm_evalMsgQp);
}

//============================================================
// Events and timing
bool Vtest::eventsPending() { return false; }

uint64_t Vtest::nextTimeSlot() {
    VL_FATAL_MT(__FILE__, __LINE__, "", "%Error: No delays in the design");
    return 0;
}

//============================================================
// Utilities

const char* Vtest::name() const {
    return vlSymsp->name();
}

//============================================================
// Invoke final blocks

void Vtest___024root___eval_final(Vtest___024root* vlSelf);

VL_ATTR_COLD void Vtest::final() {
    Vtest___024root___eval_final(&(vlSymsp->TOP));
}

//============================================================
// Implementations of abstract methods from VerilatedModel

const char* Vtest::hierName() const { return vlSymsp->name(); }
const char* Vtest::modelName() const { return "Vtest"; }
unsigned Vtest::threads() const { return 1; }
void Vtest::prepareClone() const { contextp()->prepareClone(); }
void Vtest::atClone() const {
    contextp()->threadPoolpOnClone();
}
