import Index from './components/Index.vue'
import Login from './components/Login.vue'
import Personal from './components/Personal.vue'
import PersonalData from './components/PersonalData.vue'
const routers = [
	{
	path: '/index',
	name: 'index',
	component: Index,
	children: [
		{
			path: '/',
			name: 'login',
			component: Login
		}
	]
	},
	{
		path:'/',
		component: Index,
		children: [
			{
				path: '/',
				component: Login
			}
		]
	},
	{
	path: '/personal',
	name: 'personal',
	component: Personal,
	children: [
	    {
	    	path: '/',
	    	component: Personal
	    }
		{
			path: 'personalData',
			name: 'personalData',
			component: PersonalData
		}
	]
	}
]
export default routers
