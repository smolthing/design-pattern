class Test {

    @BeforeEach
    void setup() {
        MyService myServiceMock = mock(MyService.class);
        when(myServiceMock.doSomething()).thenReturn();
    }

    static Steam<Argument> testAddSource(){
        return Stream.of(
            Argument.of(1, 1, 2),
            Argument.of(-1, 1, 0),
            Argument.of(1, -1, 0),
        );
    }

    @ParameterizedTest
    @MethodSource("testAddSource")
    public void testAdd(int input1, int input2 int expectedResult) {
        final var result = add(input);
        assertEquals(result, expectedResult);
        verify(myServiceMock, times(1)).doSomething();
        // assertNull, assertNotNull, assertTrue, assertFalse, assertThrows
    }
}