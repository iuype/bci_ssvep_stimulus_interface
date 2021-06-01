% Clear the workspace and the screen
% Author: peiyu
% Email: 1666424499@qq.com



sca;
clear;clc;
close all;
clearvars;

HideCursor;


% 被试编号
S = 1;
ratio = 0.8; % 正确率
isudp = 0;
isTrigger = 0;
udpport = 8848;

KbName('UnifyKeyNames');
escKey = KbName('ESCAPE');
running = 1;
Screen('Preference','SyncTestSettings', [0.002],[50],[0.1], [10]);
% Here we call some default settings for setting up Psychtoolbox
% PsychDefaultSetup(2);

% Get the screen numbers
screens = Screen('Screens');

% Draw to the external screen if avaliable
screenNumber = max(screens);
BLACK           = [  0,   0,   0];

% [window, windowRect] = Screen('OpenWindow', screenNumber, BLACK);
[window, windowRect] = PsychImaging('OpenWindow', screenNumber, BLACK);
ifi = Screen('GetFlipInterval', window);
[xCenter, yCenter] = RectCenter(windowRect);
winBlack = BlackIndex(window);
winWhite = WhiteIndex(window);
[screenXpixels, screenYpixels] = Screen('WindowSize', window);
Screen('TextFont', window, 'Times');

windowH = screenXpixels;
windowV = screenYpixels;
colorBackground = winBlack;
red = [winWhite winBlack winBlack]';
blue = [winBlack winBlack winWhite]';
grey = (winBlack + winWhite)/2;
colorKey = winWhite*0.25;
colorChar = winWhite;

nblk = 5;

pre_dura = 1;
ssvep_dura = 1.5;
% feed_dura = 1;
rest_dura = 0.5;
wait_dura = 60;
wait_dura2 = 10;

pre_nFrames = round(pre_dura / ifi);
ssvep_nFrames = round(ssvep_dura / ifi);
% feed_nFrames = round(feed_dura / ifi);
rest_nFrames = round(rest_dura / ifi);

waitframes = 1;
randselect = randperm(40);
target = 40;


isMarker = 0;
if isMarker
    ioObj = io64;% 初始化inpoutx64 系统驱动接口
    status = io64(ioObj);% 如果status = 0, 就可以往硬件端口读写数据。例如：我们可以向并口（LPT1）发送“1”。
    address = hex2dec('0378'); % 标准 LPT1输出端口地址
    io64(ioObj, address, 0);
end


colorForEachFrame = cell(round(ssvep_nFrames), 1);
Frequences = [
    8.0, 9.0, 10.0, 11.0, 12.0, 13.0, 14.0, 15.0,
    8.2, 9.2, 10.2, 11.2, 12.2, 13.2, 14.2, 15.2,
    8.4, 9.4, 10.4, 11.4, 12.4, 13.4, 14.4, 15.4,
    8.6, 9.6, 10.6, 11.6, 12.6, 13.6, 14.6, 15.6,
    8.8, 9.8, 10.8, 11.8, 12.8, 13.8, 14.8, 15.8,
    ];
Phrases = [
    0.0,  1.75, 1.50, 1.25, 1.0,  0.75, 0.50, 0.25,
    0.35, 0.10, 1.85, 1.60, 1.35, 1.10, 0.85, 0.60,
    0.70, 0.45, 0.20, 1.95, 1.70, 1.45, 1.20, 0.95,
    1.05, 0.80, 0.55, 0.30, 0.05, 1.80, 1.55, 1.30,
    1.40, 1.15, 0.90, 0.65, 0.40, 0.15, 1.90, 1.65,
    ];




text_dict = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
    'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
    'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
    'Y', 'Z' ,'0', '1', '2', '3', '4', '5',
    '6', '7', '8', '9', ' ', ',', '.', '<',
    };

for idx = 1:ssvep_nFrames
    colorset = [];
    for i = 1:5
        for j = 1:8
            Amp = sin(2*pi*Frequences(i, j)*idx*ifi  + Phrases(i, j)*pi);
            Amp = (Amp + 1) / 2;
            Amp = Amp* (winWhite - winBlack);
            colorset = cat(2,colorset, [ Amp, Amp , Amp]');
        end
    end
    colorForEachFrame{idx} = colorset;
end

spaceratio = 0.85;
RectSizeH = windowH/8 * spaceratio;
RectSizeV = windowV/6 * spaceratio;

TextSize = 32;
Screen('TextSize', window, TextSize);

baseRect = [0 0 RectSizeH RectSizeV];
allRects = zeros(4,40);
for i = 1:5
    for j = 1:8
        allRects(:, (i-1)*8 + j ) = CenterRectOnPointd(baseRect, j* windowH/8 - windowH/16, i*windowV/6 + windowV/12);
    end
end

resultRect = CenterRectOnPointd([0 0 allRects(1, 8)-allRects(1, 1) + RectSizeH  RectSizeV], windowH/2, windowV/12);

for i = 1:5
    for j = 1:8
        [xcent ,ycent] = RectCenter( allRects(:,(i-1)*8 + j));
        charLoc{i,j} = Screen(window, 'TextBounds', text_dict{i,j});
        charLoc{i,j} = CenterRectOnPointd(charLoc{i,j}, xcent ,ycent);
    end
end


% ---------- instr ----------- %
textString = ['Openning OffScreenWindow...'];
bound = Screen(window, 'TextBounds', textString);
bound = CenterRectOnPointd(bound,xCenter,yCenter);
% DrawFormattedText(window, textString, 'center', 'center', winWhite);
Screen('DrawText', window, textString, bound(1), bound(2), winWhite);
% % Flip to the screen
Screen('Flip', window);


baseScreen = Screen(window, 'OpenOffScreenWindow', winBlack);%BLACK背景色
Screen('TextSize', baseScreen, TextSize);
Screen('TextFont', baseScreen, 'Times');
Screen('FillRect', baseScreen, colorKey, allRects);
%     Screen('FillRect', prepareScreen(frame), red, allRects(:,trag));
Screen('FillRect', baseScreen, grey, resultRect);
for i = 1:5
    for j = 1:8
        Screen('DrawText', baseScreen, text_dict{i,j}, charLoc{i,j}(1), charLoc{i,j}(2), colorChar);
    end
end

% build every frame in advance
preScreen = Screen(window, 'OpenOffScreenWindow', winBlack);%BLACK背景色
Screen('TextSize', preScreen, TextSize);
Screen('TextFont', preScreen, 'Times');


feedbackScreen = Screen(window, 'OpenOffScreenWindow', winBlack);%BLACK背景色
Screen('TextSize', feedbackScreen, TextSize);
Screen('TextFont', feedbackScreen, 'Times');


restScreen = Screen(window, 'OpenOffScreenWindow', winBlack);%BLACK背景色
Screen('TextSize', restScreen, TextSize);
Screen('TextFont', restScreen, 'Times');




ssvepScreen = zeros(ssvep_nFrames);
for frame = 1:ssvep_nFrames
    ssvepScreen(frame) = Screen(window, 'OpenOffScreenWindow', winBlack);%BLACK背景色
    Screen('TextSize', ssvepScreen(frame), TextSize);
    Screen('TextFont', ssvepScreen(frame), 'Times');
    Screen('FillRect', ssvepScreen(frame), colorForEachFrame{frame}, allRects);
    Screen('FillRect', ssvepScreen(frame), grey, resultRect);
    for i = 1:5
        for j = 1:8
            Screen('DrawText', ssvepScreen(frame), text_dict{i,j}, charLoc{i,j}(1), charLoc{i,j}(2), colorChar);
        end
    end
end

% / build every frame in advance



textString = ['any key pressed to start'];
bound = Screen(window, 'TextBounds', textString);
bound = CenterRectOnPointd(bound,xCenter,yCenter);
% DrawFormattedText(window, textString, 'center', 'center', winWhite);
Screen('DrawText', window, textString, bound(1), bound(2), winWhite);
% % Flip to the screen
Screen('Flip', window);



KbStrokeWait;

text_dictT = text_dict';
charLocT   = charLoc';

lb = [];
for blk = 1:nblk
    
    
    %%% idle start
    trialWait = tic;
    trialWait1 =tic;
%     wait_dura2 = idle_dura;
    waiting_text = ['Empty Yourself   ',num2str(0),'/' num2str(wait_dura2) 's'];
    space = KbName('space');
    
    while toc(trialWait) < wait_dura2
        if toc(trialWait1) >= 1
            waiting_text = ['Empty Yourself   ',num2str(round(toc(trialWait))),'/' num2str(wait_dura2) 's'];
            trialWait1 = tic;
        end
        [~, ~, keyCode] = KbCheck;
        if keyCode(escKey)
            running = 0;
            break;
        end
        
        bound = Screen(window, 'TextBounds', waiting_text);
        bound = CenterRectOnPointd(bound,xCenter,yCenter);
        % DrawFormattedText(window, textString, 'center', 'center', winWhite);
        Screen('DrawText', window, waiting_text, bound(1), bound(2), winWhite);
        % % Flip to the screen
        Screen('Flip', window);
    end
    
    if running  == 0
        break;
    end
    
    for trial = 1:40
        if running  == 0
            break;
        end
        
        % ---------- start prepare ----------- %
        trag = randselect(trial);
        Screen('CopyWindow', baseScreen, preScreen);
        Screen('FillRect', preScreen, red, allRects(:,trag));
        Screen('DrawText', preScreen, text_dictT{trag}, charLocT{trag}(1), charLocT{trag}(2), colorChar);
        vbl = GetSecs;
        
        tic
        for frame = 1:pre_nFrames
            [~, ~, keyCode] = KbCheck;
            if keyCode(escKey)
                running = 0;
                break;
            end
            %         vbl = Screen('Flip', window, vbl + (waitframes - 0.5) * ifi);
            Screen('CopyWindow', preScreen, window);
            Screen('Flip', window);
        end
        pretoc = toc;
        disp(['cue = ' num2str(pretoc)]);
        
        % ---------- end prepare ----------- %
        
        if running  == 0
            break;
        end
        
        % ---------- ssvep   ----------- %
        
        if isMarker
            %% mi marker
            io64(ioObj, address, trag); % 输出命令
        end
        
        
        lb(1,trial) = trag;
        vbl = GetSecs;
        tic
        for frame = 1:ssvep_nFrames
            [~, ~, keyCode] = KbCheck;
            if keyCode(escKey)
                flag = 1;
                break;
            end
            Screen('CopyWindow', ssvepScreen(frame), window);
            Screen('Flip', window);
        end
        ssveptoc = toc;
        disp(['ssvep = ' num2str(ssveptoc)]);
        % ---------- end ssvep   ----------- %
        
        if running  == 0
            break;
        end
        
        % ---------- rest   ----------- %
        Screen('CopyWindow', baseScreen, restScreen);
        
        vbl = GetSecs;
        tic
        for frame = 1:rest_nFrames
            [~, ~, keyCode] = KbCheck;
            if keyCode(escKey)
                running = 0;
                break;
            end
            Screen('CopyWindow', restScreen, window);
            Screen('Flip', window);
        end
        resttoc = toc;
        disp(['rest = ' num2str(resttoc)]);
        % ---------- end rest   ----------- %
        if running  == 0
            break;
        end
    end
    
    if running  == 0
        break;
    end
    
    
    %% wait %%%
    trialWait = tic;
    trialWait1 =tic;
    waiting_text = ['Please Take A Rest   ',num2str(0),'/' num2str(wait_dura) 's'];
    space = KbName('space');
    while toc(trialWait) < wait_dura
        [~, ~, keyCode] = KbCheck;
        if keyCode(escKey)
            break;
        end
        if toc(trialWait1) >= 1
            waiting_text = ['Please Take A Rest   ',num2str(round(toc(trialWait))),'/' num2str(wait_dura) 's'];
            trialWait1 = tic;
        end
        bound = Screen(window, 'TextBounds', waiting_text);
        bound = CenterRectOnPointd(bound,xCenter,yCenter);
        % DrawFormattedText(window, textString, 'center', 'center', winWhite);
        Screen('DrawText', window, waiting_text, bound(1), bound(2), winWhite);
        % % Flip to the screen
        Screen('Flip', window);
    end
end



b = 1;
while exist(['bak' '_' 'S' num2str(S) '_' num2str(b) '.mat'],'file')
    b = b + 1;
end

save(['bak' '_' 'S' num2str(S) '_' num2str(b) '.mat']);

% Clear the screen.
sca;
Screen('Close');
if ~isempty(instrfindall)
    fclose(instrfindall);
end
IOPort('CloseAll');