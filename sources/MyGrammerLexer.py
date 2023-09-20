# Generated from C:/Users/Andrei_Ruzaev/PycharmProjects/pythonProject/antlr/MyGrammer.g4 by ANTLR 4.13.1
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,10,63,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,2,8,7,8,2,9,7,9,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,
        4,1,4,1,5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,41,8,6,1,7,1,7,1,7,
        1,7,1,7,1,7,1,7,3,7,50,8,7,1,8,4,8,53,8,8,11,8,12,8,54,1,9,4,9,58,
        8,9,11,9,12,9,59,1,9,1,9,0,0,10,1,1,3,2,5,3,7,4,9,5,11,6,13,7,15,
        8,17,9,19,10,1,0,2,1,0,48,57,2,0,9,9,32,32,66,0,1,1,0,0,0,0,3,1,
        0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,1,0,
        0,0,0,15,1,0,0,0,0,17,1,0,0,0,0,19,1,0,0,0,1,21,1,0,0,0,3,23,1,0,
        0,0,5,25,1,0,0,0,7,27,1,0,0,0,9,29,1,0,0,0,11,31,1,0,0,0,13,40,1,
        0,0,0,15,49,1,0,0,0,17,52,1,0,0,0,19,57,1,0,0,0,21,22,5,42,0,0,22,
        2,1,0,0,0,23,24,5,47,0,0,24,4,1,0,0,0,25,26,5,43,0,0,26,6,1,0,0,
        0,27,28,5,45,0,0,28,8,1,0,0,0,29,30,5,40,0,0,30,10,1,0,0,0,31,32,
        5,41,0,0,32,12,1,0,0,0,33,34,5,104,0,0,34,35,5,101,0,0,35,36,5,108,
        0,0,36,37,5,108,0,0,37,41,5,111,0,0,38,39,5,104,0,0,39,41,5,105,
        0,0,40,33,1,0,0,0,40,38,1,0,0,0,41,14,1,0,0,0,42,43,5,98,0,0,43,
        44,5,121,0,0,44,50,5,101,0,0,45,46,5,116,0,0,46,47,5,97,0,0,47,48,
        5,116,0,0,48,50,5,97,0,0,49,42,1,0,0,0,49,45,1,0,0,0,50,16,1,0,0,
        0,51,53,7,0,0,0,52,51,1,0,0,0,53,54,1,0,0,0,54,52,1,0,0,0,54,55,
        1,0,0,0,55,18,1,0,0,0,56,58,7,1,0,0,57,56,1,0,0,0,58,59,1,0,0,0,
        59,57,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,0,61,62,6,9,0,0,62,20,1,
        0,0,0,5,0,40,49,54,59,1,6,0,0
    ]

class MyGrammerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    HELLO = 7
    BYE = 8
    INT = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'*'", "'/'", "'+'", "'-'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "HELLO", "BYE", "INT", "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "HELLO", 
                  "BYE", "INT", "WS" ]

    grammarFileName = "MyGrammer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


