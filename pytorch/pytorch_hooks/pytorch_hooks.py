# Hooks in PyTorch

# So, a hook is just a callable object with a predefined signature, which can be registered to any nn.Module object.
# When the trigger method is used on the module (i.e. forward() or backward()), 
# the module itself with its inputs and possible outputs are passed to the hook, executing before the computation proceeds to the next module.

# In PyTorch, you can register a hook as a:
#   1) forward prehook (executing before the forward pass)
#   2) forward hook (executing after the forward pass)
#   3) backward hook (executing after the backward pass)

import torch
from torchvision.models import resnet34


device = torch.device('cuda') if torch.cuda.is_available() else torch.device('cpu')

model = resnet34(pretrained=True)
model = model.to(device)


class SaveOutput:
    def __init__(self):
        self.outputs = []
        
    def __call__(self, module, module_in, module_out):
        self.outputs.append(module_out)
        
    def clear(self):
        self.outputs = []

# An instance of SaveOutput will simply record the output tensor of the forward pass and stores it in a list.

save_output = SaveOutput()

# A forward hook can be registered with the register_forward_hook(hook) method.
# For the other types of hooks, we have register_backward_hook and register_forward_pre_hook.
# The return value of these methods is the hook handle, which can be used to remove the hook from the module.

hook_handles = []

for layer in model.modules():
    if isinstance(layer, torch.nn.modules.conv.Conv2d):
        handle = layer.register_forward_hook(save_output)
        hook_handles.append(handle)

# When this is done, the hook will be called after each forward pass of each convolutional layer.
# To test it out, we are going to use the following image.

from PIL import Image
from torchvision import transforms as T

image = Image.open('./imgs/cat.png')
transform = T.Compose([T.Resize((224, 224)), T.ToTensor()])
X = transform(image).unsqueeze(dim=0).to(device)

out = model(X)

print('# of saved outputs: ', len(save_output.outputs))

# By inspecting the tensors in this list, we can visualize what the network sees.
