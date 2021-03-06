# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
#
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

from aliyunsdkcore.request import RpcRequest
class ResizeClusterV2Request(RpcRequest):

	def __init__(self):
		RpcRequest.__init__(self, 'Emr', '2016-04-08', 'ResizeClusterV2')

	def get_HostGroups(self):
		return self.get_query_params().get('HostGroups')

	def set_HostGroups(self,HostGroups):
		for i in range(len(HostGroups)):	
			if HostGroups[i].get('ClusterId') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.ClusterId' , HostGroups[i].get('ClusterId'))
			if HostGroups[i].get('HostGroupId') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.HostGroupId' , HostGroups[i].get('HostGroupId'))
			if HostGroups[i].get('HostGroupName') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.HostGroupName' , HostGroups[i].get('HostGroupName'))
			if HostGroups[i].get('HostGroupType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.HostGroupType' , HostGroups[i].get('HostGroupType'))
			if HostGroups[i].get('Comment') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.Comment' , HostGroups[i].get('Comment'))
			if HostGroups[i].get('CreateType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.CreateType' , HostGroups[i].get('CreateType'))
			if HostGroups[i].get('ChargeType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.ChargeType' , HostGroups[i].get('ChargeType'))
			if HostGroups[i].get('Period') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.Period' , HostGroups[i].get('Period'))
			if HostGroups[i].get('NodeCount') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.NodeCount' , HostGroups[i].get('NodeCount'))
			if HostGroups[i].get('InstanceType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.InstanceType' , HostGroups[i].get('InstanceType'))
			if HostGroups[i].get('DiskType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.DiskType' , HostGroups[i].get('DiskType'))
			if HostGroups[i].get('DiskCapacity') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.DiskCapacity' , HostGroups[i].get('DiskCapacity'))
			if HostGroups[i].get('DiskCount') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.DiskCount' , HostGroups[i].get('DiskCount'))
			if HostGroups[i].get('SysDiskType') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.SysDiskType' , HostGroups[i].get('SysDiskType'))
			if HostGroups[i].get('SysDiskCapacity') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.SysDiskCapacity' , HostGroups[i].get('SysDiskCapacity'))
			if HostGroups[i].get('AutoRenew') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.AutoRenew' , HostGroups[i].get('AutoRenew'))
			if HostGroups[i].get('VswitchId') is not None:
				self.add_query_param('HostGroup.' + str(i + 1) + '.VswitchId' , HostGroups[i].get('VswitchId'))


	def get_ClusterId(self):
		return self.get_query_params().get('ClusterId')

	def set_ClusterId(self,ClusterId):
		self.add_query_param('ClusterId',ClusterId)