## The system extracts information from personal card
- Creating by a team of student at CTU 
- Text detection is based CTPN and text recognition is based crnn and ctc belong to vietocr systems.  
- This is a scientific research project about the topic of optical character recognition 
## Download requirement
 To download requirement, firstly you should create Virtual Environments
1. Download venv:
            ```
            python3 -m venv tutorial-env 
            ```
2. Activate venv:
            ``` 
            tutorial-env\Scripts\activate.bat
            ```
3. Download requirement in Virtual Environments:
            ``` 
            pip install -r requirement.txt
            ```

> If you have problems with step 2 because of requiring admin access, open powershell, run as admin and run this comman. It work for me!
>     Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigne         
## Download model 
   https://drive.google.com/drive/folders/1qCuRMkrO7jE1UK5n_nyrtFg0I1slWm5X?usp=sharing
   After downloading, add 2 models to the checkpoints directory for implementation
## Using
  1. Downloading the project to your pc.
  2. Add 2 model above to checkpoint folder.
  3. Downloading requirement.
  3. Run command.
            ```python main.py path/image```
            
 ## Creator
 - Nguyễn Nhĩ Thái                 >  email: nguyennhithai4620@gmail.com
 - Trương Hoàng Thuận
 - Bùi Quốc Trọng                  >  email: buiquoctrong110500@gmail.com
 - Võ Thành Long



