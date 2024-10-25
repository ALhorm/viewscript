from viewscript.std import Value

class Expression:
    def eval(self) -> Value:
        raise NotImplementedError
