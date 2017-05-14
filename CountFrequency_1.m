function [Frequency,repeat,standarddata,standardclass] = CountFrequency5000(string)
tic;%string = '1000_1020'
standarddata = [];
standardclass = [];
Frequency = [];
Frequency2 = [];
repeat = [];
repeat2 = [];
t1=clock;
maindir = 'D:\test\E5';
datapath = fullfile( ['D:\test\Estandard2\result2\tripstoppoint0_600_2014-12-20 ', string, '.csv']  )
standarddata1 = csvread(datapath);
standarddata = standarddata1;
tic;
[standardclass,standardtype]=dbscanmodifyGPSinner(standarddata,2,0.0005);
disp(['Standard DBSCAN time:',num2str(toc)]);
datapath = '';
subdir =  dir( maindir );
 
for i1 = 1 : length( subdir )
    tic;
    t2=clock;
    if( isequal( subdir( i1 ).name, '.' ) || ...
        isequal( subdir( i1 ).name, '..' ) || ...
        ~subdir( i1 ).isdir )
        continue;
    end
    if subdir( i1 ).name == string
     
        subdirpath = fullfile( maindir, subdir( i1 ).name, '*.csv' );
        datas = dir( subdirpath );
        SP = []; 
        for j1 = 1 : length( datas )
            tic;
            datapath = fullfile( maindir, subdir( i1 ).name, datas( j1 ).name  )
            M = csvread(datapath);
            SP = M;
            [class,type]=dbscanmodifyGPSinner(SP,2,0.0005);
            [tempFrequency,temprepeat,standarddata,standardclass] = CountAH(standarddata,standardclass,SP,class);
            [h,l]=size(Frequency);           
            if length(tempFrequency)>l
                Frequency2 = zeros(h+1,length(tempFrequency));
                for kk=1:h
                    Frequency2(kk,:)=[Frequency(kk,:),zeros(1,length(tempFrequency)-l)];
                end
                Frequency = Frequency2;
            end
            [hr,lr]=size(repeat);           
            if length(temprepeat)>lr
                repeat2 = zeros(h+1,length(temprepeat));
                for kk=1:h
                    repeat2(kk,:)=[repeat(kk,:),zeros(1,length(temprepeat)-lr)];
                end
                repeat = repeat2;
            end           
            Frequency(j1,:)=tempFrequency;
            repeat(j1,:)=temprepeat;
            disp(['Frequency ',num2str(j1),'loop time:',num2str(toc)]);
            disp('===================================================');
        end
    end
    disp(['T2 ',num2str(i1),'loop time:',num2str(etime(clock,t2))]);
end
disp(['Etime the total running time: ',num2str(etime(clock,t1))]);
end 


function [Frequency,repeat,standarddata,standardclass] = CountAH(standarddata,standardclass,data2,class2)
tcountAH = clock;
Frequency=0;
repeat = 0;
i2=0;
goon=0;
if max(standardclass)>0 && max(class2)>0
    while i2 < max(standardclass)
        i2=i2+1;
        for ii2=1:max(class2)
            [temp(ii2,i2)]=AH(standarddata(find(standardclass==i2),4:5),data2(find(class2==ii2),4:5));
            if temp(ii2,i2)<30
                Frequency(i2)=1;
                repeat(i2)=ii2;
                break;
            end
        end
        if i2==max(standardclass) && goon==0
            goon = 1;
            a=1:1:max(class2);
            b=sort(repeat);
            c=setdiff(a,b);
            for iii=1:length(c)
               standarddata = [standarddata;data2(find(class2==c(iii)),:)]; 
               d = (max(standardclass)+1)*ones(1,length(find(class2==c(iii))));
               standardclass = [standardclass,d];
            end
        end

        if min(temp(:,i2))<40
            Frequency(i2)=1;
        else
            Frequency(i2)=0;
            repeat(i2)=0;
        end
    end   
else
    Frequency=0;
    repeat=0;
end
disp(['countAH ',num2str(etime(clock,tcountAH))]);
end

function [averageAH]=AH(cluster1,cluster2)
tAH = clock;
if length(cluster1)~=0 && length(cluster2)~=0
    averageAH1=10000;
    averageAH2=10000;
    mindistance = 10000;
    for i3=1:length(cluster1)
        mindistance = 10000;
        for ii3=1:length(cluster2)
            tempdistance = distance(cluster1(i3,2),cluster1(i3,1),cluster2(ii3,2),cluster2(ii3,1))*pi/180*6371000;
            if tempdistance<mindistance
                mindistance = tempdistance;
            end
        end
        if mindistance > 1000
            averageAH = 10000;
            return
        end
        mindis(i3,1)=mindistance;
    end
    averageAH1 = mean(mindis);
    averageAH = averageAH1;
else
    averageAH = 10000;
end
%disp(['AH ',num2str(etime(clock,tAH))]);
end

function [class,type]=dbscanmodifyGPSinner(x,k,Eps)%x=[latitude,longitude]
tDBSCAN=clock;
kk=1200000;
clusternumber =2;
clustermean2=600;
validnumber=0;
clustervehicle=15;
abparameter=600;
clusteranomaly=[];


[m,n]=size(x);
clustermean=[];

if nargin<3 | isempty(Eps)
   [Eps]=epsilon(x,k);
end

x=[[1:m]' x];
[m,n]=size(x);
type=zeros(1,m);
class = zeros(1,m);
no=1;
touched=zeros(m,1);
for i5=1:m
    if touched(i5)==0;
       ob=x(i5,:);
       a=find(x(:,5)<(ob(5)+Eps));
       b=a(find(x(a,5)>(ob(5)-Eps)),1);
       c=b(find(x(b,6)<(ob(6)+Eps)),1);
       d=c(find(x(c,6)>(ob(6)-Eps)),1);
       ind = d;
    
       if length(ind)>1 & length(ind)<k+1  
          type(i5)=0;
          class(i5)=0;
       end
       if length(ind)==1 
          type(i5)=-1;             
          class(i5)=-1; 
          touched(i5)=1;
       end
       if length(ind)>=k+1 & length(ind)<kk; 
          type(i5)=1;
          class(ind)=ones(length(ind),1)*max(no);

          while ~isempty(ind)
                ob=x(ind(1),:);
                touched(ind(1))=1;
                ind(1)=[];
                a=find(x(:,5)<(ob(5)+Eps));
                b=a(find(x(a,5)>(ob(5)-Eps)),1);
                c=b(find(x(b,6)<(ob(6)+Eps)),1);
                d=c(find(x(c,6)>(ob(6)-Eps)),1);
                i1 = d;
                sublength=length(i1);
                if length(i1)>1
                   class(i1)=no;
                   if length(i1)>=k+1 & length(ind)<kk;
                      type(ob(1))=1;
                   else
                      type(ob(1))=0;
                   end

                   for i=1:length(i1)
                       if touched(i1(i))==0
                          touched(i1(i))=1;
                          ind=unique([ind; i1(i)]);
                          class(i1(i))=no;
                       end                    
                   end
                end
          end
          test = find(class==no);
          if length(unique(x(test,4)))>=clustervehicle
              validnumber=validnumber+1;
%               %scatter(x(test,5)',x(test,6)','.','k');
%               text(x(test(1),5)',x(test(1),6)',num2str(no));
              no=no+1; 
          else
              class(:,find(class==no))=-no;
          end
       end
    end
   
end

i1=find(class==0);
class(i1)=-1;
type(i1)=-1;
validnumber
disp(['dbscanmodifyGPSinner ',num2str(etime(clock,tDBSCAN))]);
end

%...........................................
function [Eps]=epsilon(x,k)
% Function: [Eps]=epsilon(x,k)
%
% Aim: 
% Analytical way of estimating neighborhood radius for DBSCAN
%
% Input: 
% x - data matrix (m,n); m-objects, n-variables
% k - number of objects in a neighborhood of an object
% (minimal number of objects considered as a cluster)
[m,n]=size(x);

Eps=((prod(max(x(:,5:6))-min(x(:,5:6)))*k*gamma(.5*n+1))/(m*sqrt(pi.^n))).^(1/n);
end


function [D]=dist(i,x)

% function: [D]=dist(i,x)
%
% Aim: 
% Calculates the Euclidean distances between the i-th object and all objects in x         
%                                                                    
% Input: 
% i - an object (1,n)
% x - data matrix (m,n); m-objects, n-variables            
%                                                                 
% Output: 
% D - Euclidean distance (m,1)

[m,n]=size(x);
for ii=1:length(x)
    D(ii,1)=distance(i(1,2),i(1,1),x(ii,2),x(ii,1))*pi/180*6371000;%单位是米
end
if n==1
   D=abs((ones(m,1)*i-x))';
end
end
