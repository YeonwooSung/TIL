# Unit testing the PyTorch code

## torch.autograd.gradcheck

To check if the model that is implemented with PyTorch, we could use the "gradchecks".

```python
from torch.autograd.gradcheck import gradcheck

def test_sanity(self):
    input = (Variable(torch.randn(20, 20).double(), requires_grad=True), )
    model = nn.Linear(20, 1).double()
    test = gradcheck(model, input, eps=1e-6, atol=1e-4)
    print(test)
```

Tip: make sure you use .double() Gradcheck will fail with only 32 bit floats.

### Related Links

[How to confirm that pytorch code is working as intended / Unit Testing a pytorch code?](https://discuss.pytorch.org/t/how-to-confirm-that-pytorch-code-is-working-as-intended-unit-testing-a-pytorch-code/16508/8)

[Interpreting gradcheck errors](https://discuss.pytorch.org/t/interpreting-gradcheck-errors/16239)

## torchtest

The [torchtest](https://github.com/suriyadeepan/torchtest) is a library that could be used for unit testing.

For more information, please read either [github repository of torchtest](https://github.com/suriyadeepan/torchtest) or [medium post](https://medium.com/@keeper6928/mltest-automatically-test-neural-network-models-in-one-function-call-eb6f1fa5019d)
